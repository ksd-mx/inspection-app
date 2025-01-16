from crewai import Agent
from typing import List
from PIL import Image

class DefectAnalyst:
    @staticmethod
    def create() -> Agent:
        return Agent(
            role="Defect Analysis Specialist",
            goal="Identify and analyze property defects from inspection photos with high accuracy",
            backstory="""You are an experienced building inspector with expertise in 
            identifying structural, electrical, plumbing, and safety issues. You have 
            extensive knowledge of building codes and standards. You excel at visual 
            analysis and can spot subtle signs of potential problems.""",
            memory=True,
            verbose=True,
            allow_delegation=False
        )

    @staticmethod
    def analyze_photos(agent: Agent, photos: List[Image.Image], room_context: dict) -> dict:
        """Process photos and identify defects"""
        task = Task(
            description=f"""Analyze these photos for any defects, damages, or code violations.
            Room Context: {room_context}
            
            For each defect identified, provide:
            1. Severity (Critical, Major, Minor)
            2. Category (Structural, Electrical, Plumbing, etc.)
            3. Detailed description
            4. Specific recommendations
            5. Location in the room
            
            Return results in a structured format.""",
            expected_output="A dictionary containing defect analysis results"
        )
        
        return agent.execute_task(task)