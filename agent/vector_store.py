from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.docs = []

    def add_documents(self, documents):
        embeddings = self.model.encode(documents)
        self.index.add(embeddings)
        self.docs.extend(documents)

    def search(self, query, k=3):
        q_embed = self.model.encode([query])
        distances, indices = self.index.search(q_embed, k)
        return [self.docs[idx] for idx in indices[0] if idx < len(self.docs)]
