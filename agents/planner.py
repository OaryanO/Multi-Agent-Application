import json
import re
from llm.groq_client import get_llm
from state import AgentState

llm = get_llm()

def extract_json(text: str):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise ValueError("No JSON found in model output")

def planner_agent(state: AgentState):
    prompt = f"""
You are the Planner Agent.

Return ONLY valid JSON.
Do not include explanations.
Do not include markdown.
Do not include text before or after JSON.

User Task:
{state['query']}

Tools:
- search(query)
- weather(city)

JSON format:
{{
  "goal": "string",
  "steps": [
    {{
      "tool": "search",
      "input": {{"query": "string"}}
    }}
  ]
}}
"""

    response = llm.invoke(prompt)
    content = response.content.strip()

    try:
        plan = json.loads(content)
    except:
        plan = extract_json(content)

    return {"plan": plan}
