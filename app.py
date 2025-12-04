import streamlit as st
from agent.researcher import ResearchAgent

st.title("🤖 AI Research & Summarization Agent")
st.write("Enter a topic/question and get RAG-based summarized answers.")

query = st.text_input("Enter your Question:")

if st.button("Search"):
    if query.strip():
        agent = ResearchAgent()

        with st.spinner("Researching..."):
            summary = agent.query(query)

        st.success("Summary:")
        st.write(summary)
