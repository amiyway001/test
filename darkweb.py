import requests
from bs4 import BeautifulSoup

def search_darkweb():
    import requests
    from bs4 import BeautifulSoup

    query = input("Enter The Query: ")

    try:
        r = requests.get(f"https://ahmia.fi/search/?q={query}", timeout=10)
        r.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    soup = BeautifulSoup(r.text, 'html.parser')

    for a in soup.find_all('a', href=True):
        title = a.text.strip() if a.text else ""
        print(f"Title: {title}, Link: {a['href']}")


search_darkweb()