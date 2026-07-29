import requests

def fetch_request():
    url = "https://api.nbp.pl/api/exchangerates/tables/C/"
    response = requests.get(url)
    response.raise_for_status()
    return response
