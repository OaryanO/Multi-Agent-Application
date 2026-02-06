import streamlit as st
from dotenv import load_dotenv
from graph import build_graph

load_dotenv()

st.set_page_config(page_title="AI Operations Assistant", page_icon="🤖")
st.title("🤖 AI Operations Assistant")

query = st.text_area(
    "Enter a task",
    placeholder="Check today’s weather in Varanasi and suggest a date plan"
)

if st.button("Run Assistant"):
    if not query.strip():
        st.warning("Please enter a task.")
    else:
        graph = build_graph()

        with st.spinner("Running Planner → Executor → Verifier..."):
            result = graph.invoke({"query": query})

        st.subheader("🧠 Planner Output")
        st.json(result["plan"])

        st.subheader("🛠 Executor Output")
        st.json(result["tool_results"])

        st.subheader("✅ Final Answer")
        st.success(result["final_answer"])
