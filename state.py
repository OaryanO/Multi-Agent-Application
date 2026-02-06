from typing import TypedDict, Dict, Any, List

class AgentState(TypedDict):
    query: str
    plan: Dict[str, Any]
    tool_results: List[Dict[str, Any]]
    final_answer: str
