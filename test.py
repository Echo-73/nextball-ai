from dotenv import load_dotenv
load_dotenv()

from what_next_agent.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

runner = Runner(
    agent=root_agent,
    app_name="what_next_app",
    session_service=InMemorySessionService()
)

query = """
Runs: 170
Wickets: 5
Overs: 19
Target: 185
Last over runs: 8
"""

try:
    response = runner.run(input=query)

    print("\nAGENT RESPONSE:")
    print(response)

    try:
        print("\nPARSED OUTPUT:")
        print(response.output)
    except:
        pass

except Exception as e:
    print("ERROR:", e)