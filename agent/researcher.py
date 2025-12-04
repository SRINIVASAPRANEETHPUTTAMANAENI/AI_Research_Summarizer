from .tools import web_search
from .summarizer import SummarizerAgent
from .vector_store import VectorStore

class ResearchAgent:
    def __init__(self):
        self.summarizer = SummarizerAgent()
        self.vector_store = VectorStore()

    def query(self, question):
        search_results = web_search(question)

        docs = [r["content"] for r in search_results if r["content"]]
        if docs:
            self.vector_store.add_documents(docs)

        context = "\n\n".join(self.vector_store.search(question))

        final_text = question + "\n\n" + context
        return self.summarizer.summarize(final_text)
