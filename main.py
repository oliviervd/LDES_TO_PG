from src.utils.utils import fetch_json
import argparse

#todo: add archive
keys = ["DMG", "HVA", "STAM", "IM", "THES", "AGENT", "ARCH"]

#TODO: make function so that it only fetches updates made since last day.
#TODO: define function that fetches all lists
#TODO: redefine function to be ASYNC

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", help="choose collections to fetch", choices=["DMG", "IM", "STAM", "HVA",
                                                                                "ARCHIEF", "THESAURUS", "AGENTS"])
    parser.add_argument("--timestamp", default = "2021-01-01T15:48:12.309Z")
    parser.add_argument("--result", choices=["pg", "csv", "xlsx"])
    args = parser.parse_args()

    #IM + HVA; laatste maal 28-08
    #STAM; 30-08

    try:
        #fetch_json("IM")
        #print("IM fetched")
        fetch_json("DMG")
        print("DMG fetched")
        #fetch_json("HVA")
        #print("HVA fetched")
        # fetch_json("STAM")
        # print("STAM fetched")
        # fetch_json("ARCH")
        # print("ARCH fetched")
        # fetch_json("AGENT")
        # print("AGENTS fetched")
        # fetch_json("THES")
        # print("THES fetched")

    except Exception:
        pass
