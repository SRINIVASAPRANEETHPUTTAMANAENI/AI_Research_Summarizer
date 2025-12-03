import os
from dotenv import load_dotenv
from transformers import pipeline
from sentence_transformers import SentenceTransformer

load_dotenv()

class HFSummarizer:
    def __init__(self, model="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model)

    def summarize(self, text, max_length=150):
        return self.summarizer(text, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']

class HFEmbeddings:
    def __init__(self, model="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model)

    def embed_documents(self, texts):
        return self.model.encode(texts, convert_to_numpy=True)
