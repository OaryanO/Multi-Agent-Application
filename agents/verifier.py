from llm.groq_client import get_llm
from state import AgentState

llm = get_llm()

def verifier_agent(state: AgentState):
    prompt = f"""
You are the Verifier Agent.

User Task:
{state['query']}

Tool Results:
{state['tool_results']}

Produce final answer.
"""
    response = llm.invoke(prompt)
    return {"final_answer": response.content}
