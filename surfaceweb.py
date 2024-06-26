from serpapi import GoogleSearch

def search_surfaceweb(query):
    
        params = {
            "q": query,
            "hl": "en",
            "gl": "us",
            "google_domain": "google.com",
            "api_key": "44badf285bae0256ec5c3ce7433dc4d0b9b0022a15594bf50336674d2d63eb27"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

    
        links = [result["link"] for result in results["organic_results"]]

        return links
