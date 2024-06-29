import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller
import time

def get_tor_session():
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    return session

def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_password')  # Replace with your actual Tor control password
        controller.signal(Signal.NEWNYM)
        time.sleep(5)

def search_darkweb_site(query, url):
    try:
        session = get_tor_session()
        r = session.get(url, params={'q': query}, timeout=30)
        r.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

    soup = BeautifulSoup(r.text, 'html.parser')
    results = []

    for a in soup.find_all('a', href=True):
        title = a.text.strip() if a.text else ""
        results.append({'title': title, 'link': a['href']})

    return results

def search_darkweb():
    query = input("Enter The Query: ")

    # List of dark web search engine URLs
    darkweb_search_engines = [
        "http://3bbad7fauom4d6sgppalyqddsqbf5u5p56b5k5uk2zxsy3d6ey2jobad.onion",
        "http://l4rsciqnpzdndt2llgjx3luvnxip7vbyj6k6nmdy4xs77tx6gkd24ead.onion",
        "http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion",
        "http://3fzh7yuupdfyjhwt3ugzqqof6ulbcl27ecev33knxe3u7goi3vfn2qqd.onion",
        "http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion",
        "http://tor66sewebgixwhcqfnp5inzp5x5uohhdy3kvtnyfxc2e5mxiuh34iid.onion",
        "http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion"
    ]

    # Search on dark web search engines
    for engine in darkweb_search_engines:
        renew_tor_ip()
        results = search_darkweb_site(query, engine)
        print(f"\nResults from {engine}:")
        for result in results:
            print(f"Title: {result['title']}, Link: {result['link']}")

if __name__ == "__main__":
    search_darkweb()
