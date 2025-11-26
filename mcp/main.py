import asyncio
from dotenv import load_dotenv
from agent import root_agent
from google.adk.runners import InMemoryRunner
load_dotenv()

async def main():
    print("Hello from mcp!")
    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug("What is the sum of 8 and 32?")
    print("Response:", response)


if __name__ == "__main__":
    asyncio.run(main())
    # 
