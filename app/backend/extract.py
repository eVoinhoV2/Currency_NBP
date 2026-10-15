import requests, json
from datetime import date

def fetch_request():
    url = "https://api.nbp.pl/api/exchangerates/tables/C/"
    response = requests.get(url)
    response.raise_for_status()
    return response

def get_data_into_json():
    response = fetch_request()
    response_json = response.json()
    with open(f"../data/{date.today()}.json", 'w') as f:
        f.write(json.dumps(response_json, indent=2))


