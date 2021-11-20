from wikidata.client import Client as WikidataClient
import requests

_Q = "Q1409014"

def add_biography(_Q):
    match = False
    wikidata_search_response = requests.get(
        'https://wikidata.org/w/api.php',
        params={
            'action': 'wbsearchentities',
            'format': 'json',
            'language': 'nl',
            'search': _Q,
        },
    ).json()

    _Qresp = wikidata_search_response

    for i in _Qresp["search"]:
        print("🥳 GOT IT 🥳")
        try:
            print("I found " + i['label'] + " on Wikidata")
        except Exception:
            pass

add_biography(_Q)