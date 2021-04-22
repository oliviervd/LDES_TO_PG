import time
import asyncio
import subprocess

today = time.time()


fetch_from = "2021-01-01T15:48:12.309Z"

endpoints = {
    "DMG": f"actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
               f"/Users/huynslol/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z --emitMemberOnce "
               f"true https://lodi.ilabt.imec.be/coghent/dmg/objecten",
    "HVA": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
               "/Users/huynslol/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z --emitMemberOnce "
               "true https://lodi.ilabt.imec.be/coghent/hva/objecten",
    "STAM": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
                "/Users/huynslol/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z --emitMemberOnce "
                "true https://lodi.ilabt.imec.be/coghent/stam/objecten",
    "IM": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
              "/Users/huynslol/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z --emitMemberOnce "
              "true https://lodi.ilabt.imec.be/coghent/industriemuseum/objecten",
    "THES": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
                "/Users/huynslol/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z --emitMemberOnce "
                "true https://lodi.ilabt.imec.be/coghent/adlib/thesaurus",
    "AGENT": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
                 "/Users/huynslol/PycharmProjects/DASHBOARD/utils/context.jsonld --fromTime 2021-01-01T15:48:12.309Z "
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

columns = ["URI", "@type", "title", "provenance", "provenance_date", "provenance_type", "material", "description", "collection"]

# fetch json based on key
async def fetch_json(key):
    with open(filepath[key], "w") as f:
        x = subprocess.run(endpoints[key], shell=True, stdout=f, text=True)
        print("Done with fetching data from {}".format(key))
        return x


# create dataframe for each database from json file
def generate_dataframe(key):
    with open(filepath[key]) as p:
        res = p.read()
        res = res.splitlines()
        # print("Done with parsing data from {}".format(key))
        return res


# fetch_title
def fetch_title(df, range, json):
    try:
        title = json["http://www.cidoc-crm.org/cidoc-crm/P102_has_title"]
        df.at[range, "title"] = title["@value"]
    except Exception:
        pass


# fetch provenance
def fetch_provenance(df, range, json):
    try:
        prov = json["MaterieelDing.isOvergedragenBijVerwerving"]
        df.at[range, "provenance"] = prov
        for x in prov:
            try:
                prov_date = x["Conditie.periode"]["Periode.einde"]
                df.at[range, "provenance_date"] = prov_date
            except Exception:
                pass
        for x in prov:
            try:
                prov_type = x["Activiteit.gebruikteTechniek"]
                for z in prov_type:
                    try:
                        prov_method = z["http://www.w3.org/2000/01/rdf-schema#label"]
                        df.at[range, "provenance_type"] = prov_method
                    except Exception:
                        pass
            except Exception:
                pass
    except Exception as e:
        pass


# fetch techniek
def fetch_techniek(df, range, json):
    try:
        material = json["MaterieelDing.bestaatUit"]
        df.at[range, "material"] = material
    except Exception as e:
        pass


# fetch collection
def fetch_collection(df, range, json):
    try:
        collection = json["MensgemaaktObject.maaktDeelUitVan"]
        collections = []
        for x in collection:
            collections.append(x["Recht.type"])
        df.at[range, "collection"] = collections
    except Exception as e:
        pass


#fetch description
def fetch_description(df, range, json):
    try:
        description = json["http://www.cidoc-crm.org/cidoc-crm/P3_has_note"]
        df.at[range, "description"] = description
    except Exception:
        pass


#[{'@type': 'Verwerving', 'Verwerving.overgedragenAan': ['http://www.wikidata.org/entity/Q1809071'], 'Verwerving.overdrachtVan': ['https://stad.gent/id/mensgemaaktobject/dmg/530026423'], 'Activiteit.gebruikteTechniek': [{'@id': 'https://stad.gent/id/concept/thesaurus/530009067', 'http://www.w3.org/2000/01/rdf-schema#label': 'oningeschreven gevonden'}], 'Conditie.periode': {'@type': 'Periode', 'Periode.einde': '2017', 'Periode.begin': '2017'}}]

