import math
from google.adk.agents import Agent


def predict_next_event(
    runs: int,
    wickets: int,
    overs: float,
    target: int,
    last_over_runs: int = 0
) -> dict:
    """
    Predict the next event in an IPL match.

    Args:
        runs (int): Current runs
        wickets (int): Wickets lost
        overs (float): Overs completed
        target (int): Target score
        last_over_runs (int): Runs scored in last over

    Returns:
        dict: Prediction output
    """
    try:
        print("TOOL CALLED", runs, wickets, overs, target, last_over_runs)

        balls_left = int((20 - overs) * 6)
        runs_needed = target - runs
        rrr = (runs_needed / balls_left) * 6 if balls_left > 0 else 0

        if rrr > 12:
            return {
                "status": "success",
                "next_event": "wicket likely",
                "wicket_probability": 0.7,
                "excitement_level": "very high",
                "fan_message": "Pressure is insane! A wicket could fall any moment!"
            }

        elif last_over_runs > 10:
            return {
                "status": "success",
                "next_event": "boundary likely",
                "wicket_probability": 0.35,
                "excitement_level": "high",
                "fan_message": "Momentum is building! Expect a big shot!"
            }

        else:
            return {
                "status": "success",
                "next_event": "dot ball or single",
                "wicket_probability": 0.15,
                "excitement_level": "medium",
                "fan_message": "Steady play, building pressure slowly."
            }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


root_agent = Agent(
    model="gemini-flash-latest",
    name="what_next_agent",
    description="Predicts what happens next in an IPL match for viewer engagement.",

    instruction="""
You are a STRICT JSON API.

You MUST ALWAYS call the tool `predict_next_event`.

Steps:
1. Extract values from user input:
   - runs
   - wickets
   - overs
   - target
   - last_over_runs

2. Call the tool exactly like:
predict_next_event(
    runs=...,
    wickets=...,
    overs=...,
    target=...,
    last_over_runs=...
)

3. Return ONLY the tool output.

IMPORTANT RULES:
- Output MUST be valid JSON
- Do NOT add explanations
- Do NOT add extra text
- Do NOT add emojis
- Do NOT rephrase anything
- Do NOT wrap JSON in text

If input is missing, respond ONLY with:
{
  "status": "error",
  "message": "Provide input as: Runs: X, Wickets: Y, Overs: Z, Target: T, Last over runs: L"
}
""",

    tools=[predict_next_event]
)