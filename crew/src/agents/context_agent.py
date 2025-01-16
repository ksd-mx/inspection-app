from crewai import Agent

def create_context_agent():
    return Agent(
        role='Inspection Context Analyst',
        goal='Analyze structural findings in the context of the property\'s history and characteristics',
        backstory="""You are a senior building inspector with expertise in 
        correlating current findings with historical property data. Your strength 
        lies in identifying patterns and predicting potential future issues.""",
        verbose=True,
        allow_delegation=True  # This agent can delegate to get additional structural analysis if needed
    )