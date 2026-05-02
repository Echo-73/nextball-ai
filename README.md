# NextBall AI

### Predicting the Next Moment in IPL

---

## Overview

NextBall AI is a viewer-focused AI system that predicts the **most likely next event** in an IPL match—such as a wicket, boundary, or dot ball—based on real-time match conditions.

Unlike traditional analytics that focus on final outcomes, this project enhances **fan engagement** by estimating what might happen next in the game.

---

## Problem

While watching IPL matches, fans constantly anticipate:

* Will a wicket fall next?
* Is a big shot coming?
* Will this over change the match?

However, existing platforms only provide **static statistics** and do not offer real-time predictive insights, making the viewing experience less interactive.

---

## Solution

This project uses a single AI agent to:

* Analyze match context (runs, wickets, overs, etc.)
* Estimate the most likely next event
* Provide excitement level and fan-friendly insights

---

## How It Works

1. User provides match details
2. AI agent extracts key parameters
3. Tool-based logic calculates match pressure
4. System predicts:

   * Next event (wicket / boundary / dot ball)
   * Wicket probability
   * Excitement level

---

## ⚙️ Tech Stack

* Python
* Google ADK (Agent Development Kit)
* Gemini API (Google AI)

---

## Project Structure

```
what_next_agent/
│
├── what_next_agent/
│   ├── __init__.py
│   └── agent.py
│
├── test.py
├── requirements.txt
├── .env
├── README.md
```

---

## How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Add your API key in `.env`

```
GOOGLE_API_KEY=your_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=0
```

### 3. Run the project

```
adk web
```

---

## Sample Input

```
Runs: 170
Wickets: 5
Overs: 19
Target: 185
Last over runs: 8
```

---

## Sample Output

```json
{
  "status": "success",
  "next_event": "wicket likely",
  "wicket_probability": 0.7,
  "excitement_level": "very high",
  "fan_message": "Pressure is insane! A wicket could fall any moment!"
}
```

---

## Key Features

* Real-time next-event prediction
* Viewer-focused AI experience
* Simple and fast single-agent system
* Structured JSON output

---

## Note

This system does not predict exact outcomes.
It estimates the **most likely next event** based on match context and pressure.

---

## Future Improvements

* Live IPL data integration
* Interactive UI dashboard
* Advanced probability models
* Player-specific predictions

---

## Author

Divija Bellapukonda

---
