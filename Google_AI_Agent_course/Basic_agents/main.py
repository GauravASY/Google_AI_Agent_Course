from dotenv import load_dotenv
import asyncio
from agent import root_agent
from google.adk.runners import InMemoryRunner


async def main():
    load_dotenv()
    print("Hello from basic-agents!")
    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug("Who is the highest run scorer in current ongoing test series between Indian and South Africa?")

if __name__ == "__main__":
    asyncio.run(main())
