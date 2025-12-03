import streamlit as st
from agent.researcher import ResearchAgent

st.set_page_config(page_title="AI Research & Summarization Agent")
st.title("🤖 AI Research & Summarization Agent")
st.write("Enter a topic/question, get summarized answers, and see retrieved knowledge via RAG!")

agent = ResearchAgent()

query = st.text_input("Enter your Question:")
if st.button("Get Summary") and query:
    with st.spinner("Searching and summarizing..."):
        summary = agent.query(query)
        st.success("✅ Summary:")
        st.write(summary)
