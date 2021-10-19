from src.utils.utils import fetch_json
import argparse
import os

#todo: add archive
keys = ["DMG", "HVA", "STAM", "IM", "THES", "AGENT", "ARCH"]

#TODO: make function so that it only fetches updates made since last day.
#TODO: define function that fetches all lists
#TODO: redefine function to be ASYNC

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='return LDES for chosen DCAT')
    parser.add_argument("--fetch", metavar="fetch", action="append", help="choose collections to fetch", choices=["DMG", "IM", "STAM", "HVA",
                                                                                "ARCHIEF", "THESAURUS", "AGENTS"])
    parser.add_argument("--timestamp", default = "2021-01-01T15:48:12.309Z")
    parser.add_argument("--result", choices=["pg", "csv", "xlsx"])
    args = parser.parse_args()

    choice = args.fetch


    #IM + HVA; laatste maal 28-08
    #STAM; 30-08

    ROOT_DIR = os.path.abspath(os.curdir)
    path = ROOT_DIR + "/data"
    if not os.path.exists(path):
        os.mkdir(path)

    for c in choice:
        try:
            fetch_json(c)
            print(str(c)+" fetched")
        except Exception:
            pass

