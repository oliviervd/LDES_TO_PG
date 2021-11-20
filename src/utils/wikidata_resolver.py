from wikidata.client import Client as WikidataClient
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

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

        try:
            print(i["description"])
        except Exception:
            pass

        print(_Qresp)

        wikidata_client = WikidataClient()

        entity = wikidata_client.get(i["id"], load=True)
        print(entity)

        try:
            i['wikipedia_url'] = entity.data['sitelinks']['enwiki']['url']
            # wikipedia extract time
            wikipedia_search_response = requests.get(
                'https://en.wikipedia.org/w/api.php',
                params={
                    'action': 'query',
                    'format': 'json',
                    'titles': entity.data['sitelinks']['enwiki']['title'],
                    'prop': 'info|extracts',
                    'exintro': True,
                    'explaintext': True,
                    'inprop': 'url',
                }
            ).json()

            try:
                wikipedia_page = next(
                    iter(wikipedia_search_response['query']['pages'].values()),
                )
                i['wikipedia_extract'] = wikipedia_page["extract"]
                print(
                    f'Wikipedia extract: {i["wikipedia_extract"]}'
                )
            except KeyError:
                pass
        except Exception:
            pass

        try:
            i['image_url'] = entity[wikidata_client.get('P18')].image_url
            print(f'Image: {i["image_url"]}')
        except KeyError:
            pass

add_biography(_Q)