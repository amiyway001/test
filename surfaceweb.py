from serpapi import GoogleSearch
from bs4 import BeautifulSoup

def search_surfaceweb():
    def get_user_input():
        q = input("Enter search query: ")

        return q

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
            link = result["link"]
            title = result["title"]
            print(f"Title: {title}, Link: {link}")

    if __name__ == "__main__":
        q = get_user_input()
        perform_search(q)


search_surfaceweb()