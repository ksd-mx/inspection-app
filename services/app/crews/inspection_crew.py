from crewai import Crew, Process
from .agents.defect_analyst import DefectAnalyst
from .agents.context_analyst import ContextAnalyst
from .agents.report_writer import ReportWriter
from PIL import Image
from typing import List, Dict

class InspectionCrew:
    def __init__(self):
        """Initialize the inspection crew with all agents"""
        self.defect_analyst = DefectAnalyst.create()
        self.context_analyst = ContextAnalyst.create()
        self.report_writer = ReportWriter.create()
        
        self.crew = Crew(
            agents=[
                self.defect_analyst,
                self.context_analyst,
                self.report_writer
            ],
            process=Process.hierarchical,
            memory=True,
            verbose=True
        )

    async def analyze_room(
        self,
        photos: List[Image.Image],
        room_context: Dict,
        previous_findings: Dict = None
    ) -> Dict:
        """
        Coordinate the analysis of room photos through all agents
        """
        # Step 1: Defect Analysis
        defect_results = DefectAnalyst.analyze_photos(
            self.defect_analyst,
            photos,
            room_context
        )

        # Step 2: Context Analysis
        context_results = ContextAnalyst.analyze_context(
            self.context_analyst,
            defect_results,
            previous_findings or {}
        )

        # Step 3: Report Generation
        report = ReportWriter.generate_report(
            self.report_writer,
            defect_results,
            context_results
        )

        # Return combined results
        return {
            "defect_analysis": defect_results,
            "context_analysis": context_results,
            "report": report
        }