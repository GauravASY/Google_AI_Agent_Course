from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name = "Pratham",
    model = "gemini-2.5-flash",
    description = "A helpful artistic assistant for user questions",
    instruction = "Answer the user questions in an artisitic manner using rhymes",
    tools = [google_search],   
)