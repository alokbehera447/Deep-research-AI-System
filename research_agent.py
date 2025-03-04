from tavily import TavilyClient

TAVILY_API_KEY = "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"
client = TavilyClient(api_key=TAVILY_API_KEY)

def search_web(query):
    results = client.search(query=query, num_results=5)
    return results  # Returns a list of scraped pages
