from transformers import pipeline
import os

class SummarizerAgent:
    def __init__(self):
        self.summarizer = pipeline("summarization")

    def summarize(self, text, max_length=150):
        summary = self.summarizer(text, max_length=max_length, min_length=30, do_sample=False)
        return summary[0]['summary_text']
