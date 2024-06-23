from serpapi import GoogleSearch

def search_surfaceweb(query):
    
        params = {
            "q": query,
            "hl": "en",
            "gl": "us",
            "google_domain": "google.com",
            "api_key": "ca57420ba8d67a1aa3ba3704ddeae271bbaa2ccd68110b1849ec94dc979724fd"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

    
        links = [result["link"] for result in results["organic_results"]]

        return links
