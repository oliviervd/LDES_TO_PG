import subprocess
import pandas as pd
from pprint import pprint
from utils import fetch_json
import asyncio

#todo: parse endpoints from DCAT https://lodi.imec.ugent/coghent/

#todo: add archive
keys = ["DMG", "HVA", "STAM", "IM", "THES", "AGENT"]

#TODO: make function so that it only fetches updates made since last day.
#TODO: define function that fetches all lists
#TODO: redefine function to be ASYNC


# async def fetch_dcat():
#     #TODO: debug; doesnt' loop?
#     for future in asyncio.as_completed(map(fetch_json(), keys)):
#         result = await future
#     print("FINISHED SYNC WITH LDES_CLIENT")
#
# loop = asyncio.new_event_loop()
# loop.run_until_complete(fetch_dcat())
#
# if __name__ == "__main__":
#     try:
#         loop = asyncio.new_event_loop()
#         loop.run_until_complete(fetch_dcat())
#     except Exception as e:
#         pass
#     finally:
#         loop.close()

if __name__ == "__main__":
    try:
        fetch_json("DMG")
        print("DMG fetched")
        fetch_json("HVA")
        print("HVA fetched")
        fetch_json("STAM")
        print("STAM fetched")
        fetch_json("IM")
        print("IM fetched")
    except Exception:
        pass




