from bs4 import BeautifulSoup
import requests

def search_darkweb(query):
    results = []  # Initialize an empty list to store results
    try:
        r = requests.get(f"https://ahmia.fi/search/?q={query}", timeout=10)
        r.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return results  # Return empty list in case of request failure

    soup = BeautifulSoup(r.text, 'html.parser')

    for a in soup.find_all('a', href=True):
        title = a.text.strip() if a.text else "No Title"
        link = a['href']
        results.append(link)  # Add the result as a dictionary to the list

    return results