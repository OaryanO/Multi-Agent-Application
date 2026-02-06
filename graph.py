from langgraph.graph import StateGraph, END
from state import AgentState
from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.verifier import verifier_agent

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_agent)
    graph.add_node("executor", executor_agent)
    graph.add_node("verifier", verifier_agent)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "verifier")
    graph.add_edge("verifier", END)

    return graph.compile()
