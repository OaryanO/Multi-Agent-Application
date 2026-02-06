import requests
import os
from dotenv import load_dotenv

load_dotenv()

CACHE = {}

def search_tool(query: str):
    if query in CACHE:
        return CACHE[query]

    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "engine": "google",
        "api_key": os.getenv("SERPAPI_API_KEY")
    }

    data = requests.get(url, params=params).json()

    result = [
        r.get("snippet")
        for r in data.get("organic_results", [])[:3]
    ]

    CACHE[query] = result
    return result
