from concurrent.futures import ThreadPoolExecutor
from state import AgentState
from tools.search import search_tool
from tools.weather import weather_tool

TOOLS = {
    "search": search_tool,
    "weather": weather_tool
}

def run_step(step):
    tool_name = step["tool"]

    if tool_name not in TOOLS:
        return {
            "tool": tool_name,
            "error": "Tool not implemented"
        }

    try:
        output = TOOLS[tool_name](**step["input"])
        return {"tool": tool_name, "output": output}
    except Exception as e:
        return {"tool": tool_name, "error": str(e)}

def executor_agent(state: AgentState):
    steps = state["plan"]["steps"]

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(run_step, steps))

    return {"tool_results": results}
