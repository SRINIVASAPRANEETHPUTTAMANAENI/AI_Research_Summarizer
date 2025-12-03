import os
from serpapi import GoogleSearch

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

def web_search(query, num_results=3):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": num_results
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    snippets = []
    if "organic_results" in results:
        for res in results["organic_results"][:num_results]:
            if "snippet" in res:
                snippets.append(res["snippet"])
    return " ".join(snippets)
