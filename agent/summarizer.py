from transformers import pipeline

class SummarizerAgent:
    def __init__(self):
        self.summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6"
        )

    def summarize(self, text):
        summary = self.summarizer(text, max_length=120, min_length=40, do_sample=False)
        return summary[0]["summary_text"]
