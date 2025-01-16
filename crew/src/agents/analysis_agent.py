from crewai import Agent
from tools.image_analyzer import StructuralImageAnalyzer
from tools.measurement_analyzer import StructuralMeasurementAnalyzer

def create_analysis_agent():
    return Agent(
        role='Structural Analysis Specialist',
        goal='Analyze structural defects with high precision and detail',
        backstory="""You are an experienced structural engineer with over 15 years 
        of experience in building diagnostics. Your expertise lies in analyzing 
        structural defects and determining their implications for building integrity.""",
        tools=[StructuralImageAnalyzer(), StructuralMeasurementAnalyzer()],
        verbose=True,
        allow_delegation=False  # This agent is a specialist who does their own analysis
    )