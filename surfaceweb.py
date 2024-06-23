from serpapi import GoogleSearch

def search_surfaceweb(query):
    def perform_search(q):
        params = {
            "q": q,
            "hl": "en",
            "gl": "us",
            "google_domain": "google.com",
            "api_key": "ca57420ba8d67a1aa3ba3704ddeae271bbaa2ccd68110b1849ec94dc979724fd"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        for result in results["organic_results"]:
            print(result["link"])
        
            
    perform_search(query)