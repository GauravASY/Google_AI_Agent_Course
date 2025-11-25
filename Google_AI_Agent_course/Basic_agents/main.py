from dotenv import load_dotenv
import asyncio
from agent import root_agent
from google.adk.runners import InMemoryRunner
from google.adk.agents.run_config import RunConfig, StreamingMode

async def main():
    load_dotenv()
    print("Hello from basic-agents!")
    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug("Who is the highest run scorer in current ongoing test series between Indian and South Africa?",  run_config= RunConfig(
    streaming_mode=StreamingMode.SSE,
    max_llm_calls=200))

if __name__ == "__main__":
    asyncio.run(main())
