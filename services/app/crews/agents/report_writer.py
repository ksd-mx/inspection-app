from crewai import Agent
from typing import Dict

class ReportWriter:
    @staticmethod
    def create() -> Agent:
        return Agent(
            role="Technical Documentation Specialist",
            goal="Create professional, clear, and actionable inspection reports",
            backstory="""You are an expert technical writer with years of experience 
            in property inspection documentation. You excel at converting technical 
            findings into clear, professional reports that both experts and laypeople 
            can understand.""",
            memory=True,
            verbose=True,
            allow_delegation=True
        )

    @staticmethod
    def generate_report(
        agent: Agent, 
        defect_analysis: Dict, 
        context_analysis: Dict
    ) -> dict:
        """Generate professional report from analyses"""
        task = Task(
            description=f"""Create a professional report segment based on the analyses provided.
            Defect Analysis: {defect_analysis}
            Context Analysis: {context_analysis}
            
            Include:
            1. Clear descriptions of findings
            2. Severity assessments
            3. Technical details in accessible language
            4. Prioritized recommendations
            5. Next steps
            
            Format the report professionally and ensure it's actionable.""",
            expected_output="A dictionary containing the formatted report"
        )
        
        return agent.execute_task(task)