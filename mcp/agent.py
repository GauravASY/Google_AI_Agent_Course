from google.adk.agents.llm_agent import Agent
from tools import add_tool


root_agent = Agent(
    name = "Dwitiya",
    model = "gemini-2.5-flash",
    description = "An expert tutor for teaching complex subjects in intuitve manner using real world examples.",
    instruction =" You are an expert tutor with a decade of experience in teaching and mentoring. Your task is to help users understand complex topics in intuitive manner using real world examples.",
    tools = [add_tool]
)