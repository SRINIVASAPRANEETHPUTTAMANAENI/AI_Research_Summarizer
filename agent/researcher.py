import os
from .tools import web_search
from .summarizer import SummarizerAgent
from sentence_transformers import SentenceTransformer

class ResearchAgent:
    def __init__(self):
        self.summarizer = SummarizerAgent()
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")  # lightweight embedding model

    def query(self, question):
        # Step 1: Get web search results
        results = web_search(question)
        if not results:
            return "No relevant search results found."

        # Step 2: Summarize the results
        summary = self.summarizer.summarize(results)
        return summary
