from agent import root_agent
from google.adk.runners import InMemoryRunner

def main():
    print("Hello from mcp!")
    runner = InMemoryRunner(agent=root_agent)
    response = runner.run(input="What is the sum of 8 and 32?")
    print("Response:", response)


if __name__ == "__main__":
    main()
