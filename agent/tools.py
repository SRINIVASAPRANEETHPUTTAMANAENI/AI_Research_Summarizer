import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

def web_search(query):
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError("TAVILY_API_KEY missing from .env")

    client = TavilyClient(api_key=api_key)

    response = client.search(query=query)

    results = []
    for r in response.get("results", []):
        results.append({
            "title": r.get("title", ""),
            "url": r.get("url", ""),
            "content": r.get("content", "")
        })

    return results
