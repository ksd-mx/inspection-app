from crewai import Agent
from typing import Dict

class ContextAnalyst:
    @staticmethod
    def create() -> Agent:
        return Agent(
            role="Pattern Recognition Specialist",
            goal="Analyze defects in broader property context and identify patterns",
            backstory="""You are a senior property inspector who specializes in 
            understanding how different property issues relate to each other and 
            their broader implications. You excel at identifying patterns and 
            predicting potential future issues based on current findings.""",
            memory=True,
            verbose=True,
            allow_delegation=True
        )

    @staticmethod
    def analyze_context(agent: Agent, current_defects: Dict, previous_findings: Dict) -> dict:
        """Analyze defects in context of previous findings"""
        task = Task(
            description=f"""Review these new defects and analyze them in context of previous findings.
            Current Defects: {current_defects}
            Previous Findings: {previous_findings}
            
            Provide:
            1. Pattern identification
            2. Related issues across rooms
            3. Risk assessment
            4. Broader implications
            5. Priority recommendations
            
            Return a structured analysis.""",
            expected_output="A dictionary containing contextual analysis"
        )
        
        return agent.execute_task(task)