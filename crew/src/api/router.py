from fastapi import APIRouter, HTTPException
from .schemas import InspectionRequest, InspectionResponse
from crewai import Task, Crew, Process, LLM
from agents.analysis_agent import create_analysis_agent
from agents.context_agent import create_context_agent
from agents.reporter_agent import create_reporter_agent

from models.property_context import PropertyContext, PropertyIssue

router = APIRouter()

@router.post("/inspect", response_model=InspectionResponse)
async def create_inspection(request: InspectionRequest) -> InspectionResponse:
    try:
        # Configure LLM
        llm = LLM(model="gpt-3.5-turbo")
        llm.set_verbose = True

        # Sample property context
        property_context = PropertyContext(
            address="123 Sample Street",
            year_built=1985,
            foundation_type="poured concrete",
            last_inspection_date="2023-06-15",
            previous_issues=[
                PropertyIssue(
                    date="2022-03-10",
                    type="minor foundation crack",
                    location="south wall",
                    resolved=True,
                    resolution_details="Sealed with epoxy injection"
                )
            ],
            soil_type="clay",
            climate_zone="humid continental",
            building_materials={"foundation": "concrete", "walls": "brick"}
        )

        # Create agents
        structural_analyst = create_analysis_agent()
        context_analyst = create_context_agent()
        inspection_reporter = create_reporter_agent()
        
        for agent in [structural_analyst, context_analyst, inspection_reporter]:
            agent.llm = llm

        # Define tasks with clear collaboration points
        structural_analysis_task = Task(
            description=f"""Analyze the structural defect in the provided image.
            1. Use the StructuralImageAnalyzer tool to assess the defect
            2. Use the StructuralMeasurementAnalyzer to evaluate measurements
            3. Provide initial severity assessment
            
            Location: {property_context.address}
            Image path: basement_wall_crack.jpg""",
            expected_output="Detailed structural analysis with measurements, characteristics, and severity assessment",
            agent=structural_analyst
        )

        context_analysis_task = Task(
            description=f"""Based on the structural analysis and this property context:
            {property_context.dict()}
            
            1. Review the structural findings in context of property history
            2. Identify any patterns or recurring issues
            3. Assess the risk level considering all factors
            4. Note any environmental or seasonal factors that may be relevant""",
            expected_output="Comprehensive context analysis with risk assessment and pattern identification",
            agent=context_analyst
        )

        report_generation_task = Task(
            description="""Using both the structural analysis and context assessment:
            1. Create a detailed inspection report section
            2. Prioritize findings based on severity and risk
            3. Provide clear, actionable recommendations
            4. Include any necessary follow-up inspection requirements
            5. Add maintenance suggestions to prevent future issues""",
            expected_output="Professional inspection report with findings, recommendations, and follow-up actions",
            agent=inspection_reporter
        )

        # Create crew with hierarchical process
        inspection_crew = Crew(
            agents=[structural_analyst, context_analyst, inspection_reporter],
            tasks=[structural_analysis_task, context_analysis_task, report_generation_task],
            verbose=True,
            process=Process.sequential
        )

        # Execute inspection
        result = inspection_crew.kickoff()

        # Structure the response
        return InspectionResponse(
            structural_analysis={"result": str(result)},  # You might want to parse this better
            context_analysis={"property_data": request.property_data},
            report={"final_report": str(result)},
            metadata={
                "model_used": "gpt-3.5-turbo",
                "process_type": "sequential"
            },
            additional_data=request.additional_context
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))