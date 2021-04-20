import time
import asyncio
import subprocess

today = time.time()


fetch_from = "2021-01-01T15:48:12.309Z"

endpoints = {
    "DMG": f"actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
               f"/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z --emitMemberOnce "
               f"true https://lodi.ilabt.imec.be/coghent/dmg/objecten",
    "HVA": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
               "/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z --emitMemberOnce "
               "true https://lodi.ilabt.imec.be/coghent/hva/objecten",
    "STAM": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
                "/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z --emitMemberOnce "
                "true https://lodi.ilabt.imec.be/coghent/stam/objecten",
    "IM": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
              "/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z --emitMemberOnce "
              "true https://lodi.ilabt.imec.be/coghent/industriemuseum/objecten",
    "THES": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
                "/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z --emitMemberOnce "
                "true https://lodi.ilabt.imec.be/coghent/adlib/thesaurus",
    "AGENT": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
                 "/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z "
                 "--emitMemberOnce true https://lodi.ilabt.imec.be/coghent/adlib/personen"
}

filepath = {
    "DMG": "/Users/huynslol/PycharmProjects/DASHBOARD/data/dmg_obj.json",
    "HVA": "/Users/huynslol/PycharmProjects/DASHBOARD/data/hva_obj.json",
    "STAM": "/Users/huynslol/PycharmProjects/DASHBOARD/data/stam_obj.json",
    "IM": "/Users/huynslol/PycharmProjects/DASHBOARD/data/im_obj.json",
    "THES": "/Users/huynslol/PycharmProjects/DASHBOARD/data/thes.json",
    "AGENT": "/Users/huynslol/PycharmProjects/DASHBOARD/data/agents.json"
}


# fetch json based on key
async def fetch_json(key):
    with open(filepath[key], "w") as f:
        x = subprocess.run(endpoints[key], shell=True, stdout=f, text=True)
        print("Done with fetching data from {}".format(key))
        return x


# create dataframe for each database from json file
async def generate_dataframe(key):
    with open(filepath[key]) as p:
        res = p.read()
        res = res.splitlines()
        print("Done with parsing data from {}".format(key))
        return res


# fetch_title
# async def fetch_title():
#     try:
#         title = j["http://www.cidoc-crm.org/cidoc-crm/P102_has_title"]
#     except Exception:
#         pass
