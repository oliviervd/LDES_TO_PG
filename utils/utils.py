# {"@context":["https://data.vlaanderen.be/doc/applicatieprofiel/cultureel-erfgoed-object/kandidaatstandaard/2020-07-17/context/cultureel-erfgoed-object-ap.jsonld","https://data.vlaanderen.be/context/persoon-basis.jsonld","https://brechtvdv.github.io/demo-data/cultureel-erfgoed-event-ap.jsonld",{"dcterms:isVersionOf":{"@type":"@id"},"prov":"http://www.w3.org/ns/prov#"}],"@id":"https://stad.gent/id/mensgemaaktobject/dmg/530026423/2021-05-21T17:12:34.363Z","@type":"MensgemaaktObject","http://purl.org/dc/terms/isVersionOf":{"@id":"https://stad.gent/id/mensgemaaktobject/dmg/530026423"},"http://www.cidoc-crm.org/cidoc-crm/P102_has_title":{"@language":"nl","@value":"Doorzichtig waterreservoir"},"MaterieelDing.isOvergedragenBijVerwerving":[{"@type":"Verwerving","Verwerving.overgedragenAan":["http://www.wikidata.org/entity/Q1809071"],"Verwerving.overdrachtVan":["https://stad.gent/id/mensgemaaktobject/dmg/530026423"],"Activiteit.gebruikteTechniek":[{"@id":"https://stad.gent/id/concept/530009067"..

import time
import asyncio
import subprocess
from datetime import datetime
import pandas as pd

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

columns_obj = ["URI", "timestamp", "@type", "owner", "title", "object_name", "creator", "creator_role", "creation_place",  "provenance_date", "provenance_type", "material", "description", "collection", "association"]

# fetch json based on key
def fetch_json(key):
    with open(filepath[key], "w") as f:
        p = subprocess.run(endpoints[key], shell=True, stdout=f, text=True)

# fetch_owner
def fetch_owner(df, range, json):
    try:
        owner = json["MaterieelDing.beheerder"]
        df.at[range, "owner"] = owner
    except Exception:
        pass

# fetch_title
def fetch_title(df, range, json):
    try:
        title = json["http://www.cidoc-crm.org/cidoc-crm/P102_has_title"]
        df.at[range, "title"] = title["@value"]
    except Exception:
        pass

def generate_dataframe(key):
    with open(filepath[key]) as p:
        res = p.read()
        res = res.splitlines()
        print("Done with parsing data from {}".format(key))
        # print("Done with parsing data from {}".format(key))
        return res

# fetch provenance
# [{'@type': 'Verwerving', 'Verwerving.overgedragenAan': ['http://www.wikidata.org/entity/Q1809071'], 'Verwerving.overdrachtVan': ['https://stad.gent/id/mensgemaaktobject/dmg/530027439']}]

def fetch_provenance(df, range, json):
    try:
        prov = json["MaterieelDing.isOvergedragenBijVerwerving"]
        # df.at[range, "provenance"] = prov
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
                        prov_method = z["skos:prefLabel"]["@value"]
                        df.at[range, "provenance_type"] = prov_method
                    except Exception:
                        pass
            except Exception:
                pass
    except Exception as e:
        pass


# fetch techniek
# [{'@type': 'MaterieelDing', 'MensgemaaktObject.materiaal': {'@id': 'http://vocab.getty.edu/aat/300010900', 'skos:prefLabel': {'@language': 'nl', '@value': 'metaal'}}}, {'@type': 'MaterieelDing', 'MensgemaaktObject.materiaal': {'@id': 'http://vocab.getty.edu/aat/300014570', 'skos:prefLabel': {'@language': 'nl', '@value': 'kunststof'}}}, {'@type': 'MaterieelDing', 'MensgemaaktObject.materiaal': 'http://vocab.getty.edu/aat/300014570'}]
#[{'@type': 'MaterieelDing', 'MensgemaaktObject.materiaal': {'@id': 'https://stad.gent/id/concept/530010226', 'skos:prefLabel': {'@language': 'nl', '@value': 'polycarbonate (pp)'}}}, {'@type': 'MaterieelDing', 'MensgemaaktObject.materiaal': {'@id': 'https://stad.gent/id/concept/530010183', 'skos:prefLabel': {'@language': 'nl', '@value': 'polymethacrylimide (pp)'}}}, {'@type': 'MaterieelDing', 'MensgemaaktObject.materiaal': {'@id': 'https://stad.gent/id/concept/530010161', 'skos:prefLabel': {'@language': 'nl', '@value': 'polyamide (pp)'}}}, {'@type': 'MaterieelDing', 'MensgemaaktObject.materiaal': {'@id': 'https://stad.gent/id/concept/530010260', 'skos:prefLabel': {'@language': 'nl', '@value': 'natural rubber (pp)'}}}]

def fetch_material(df, range, json):
    try:
        material = json["MaterieelDing.bestaatUit"]
        materials = []
        for m in material:
            materials.append(m["MensgemaaktObject.materiaal"]["skos:prefLabel"]["@value"])
        df.at[range, "material"] = materials
    except Exception as e:
        pass


# fetch collection
#[[{'@id': 'http://vocab.getty.edu/aat/300257284', 'http://www.w3.org/2000/01/rdf-schema#label': {'@language': 'nl', '@value': 'huishoudelijke apparaten (ok)'}}], [{'@id': 'https://stad.gent/id/concept/530009137', 'http://www.w3.org/2000/01/rdf-schema#label': {'@language': 'nl', '@value': 'Nova'}}]]
def fetch_collection(df, range, json):
    try:
        collection = json["MensgemaaktObject.maaktDeelUitVan"]
        collections = []
        coll=[]
        for x in collection:
            c= x["Recht.type"]
            for col in c:
                # print(col["http://www.w3.org/2000/01/rdf-schema#label"]["@value"])
                collections.append(col["http://www.w3.org/2000/01/rdf-schema#label"]["@value"])
        df.at[range, "collection"] = collections
    except Exception as e:
        pass


#fetch description
def fetch_description(df, range, json):
    try:
        description = json["http://www.cidoc-crm.org/cidoc-crm/P3_has_note"]["@value"]
        df.at[range, "description"] = description
    except Exception:
        pass


def fetch_timestamp(df, range, json):
    try:
        time_stamp = json["@id"]
        time_stamp = time_stamp.split("/")[-1]
        df.at[range, "timestamp"] = time_stamp
    except Exception:
        pass

#[{'@id': 'https://stad.gent/id/entiteit/530001198', '@type': 'Agent', 'http://www.w3.org/2000/01/rdf-schema#label': {'@language': 'nl', '@value': 'Nova'}}]

def fetch_creator(df, range, json):
    try:
        creator = json["MaterieelDing.productie"]["Activiteit.uitgevoerdDoor"]
        creators = []
        for c in creator:
            creators.append(c["http://www.w3.org/2000/01/rdf-schema#label"]["@value"])
        df.at[range, "creator"] = creators
    except Exception:
        pass


def fetch_creator_place(df, range, json):
    try:
        creation_place = json["MaterieelDing.productie"]["Gebeurtenis.plaats"]
        c_places = []
        for place in creation_place:
            c_places.append(place["skos:prefLabel"]["@value"])
        df.at[range, "creation_place"] = c_places
    except Exception:
        pass

#TODO: fetch_creator_role
# [{'@id': 'https://stad.gent/id/entiteit/530001198', '@type': 'Agent', 'http://www.w3.org/2000/01/rdf-schema#label': {'@language': 'nl', '@value': 'Nova'}}]
def fetch_creator_role(df, range, json):
    try:
        creator_role = json["MaterieelDing.productie"]
        df.at[range, "creator_role"] = creator_role
    except Exception:
        pass

# OBJECTNAAM
def fetch_objectname(df, range, json):
    try:
        object_names = []
        obj_n = []
        # object_names.append(json["Entiteit.classificatie"])
        try:
            # for i in object_names:
            #     for x in i:
            #         obj_n.append(x["Classificatie.toegekendType"])
            #         # print(x["Classificatie.toegekendType"])
            for i in json["Entiteit.classificatie"]:
                for a in i["Classificatie.toegekendType"]:
                    on = a["skos:prefLabel"]["@value"]
                    object_names.append(on)
                    df.at[range, "object_name"] = object_names
            # for obj in obj_n:
                # print(type(obj[1]))
                # print(obj[1])
            # for i in object_names:
            #     obj_n.append(json["Classificatie.toegekendType"])
            #     print(object_names)

        except Exception:
            pass

        # print(object_names)

    except Exception:
        pass


def fetch_association(df, range, json):
    try:
        associations = []
        for i in json["MensgemaaktObject.draagt"]:
            for a in i["Werk.gaatOver"]:
                ass = a["skos:prefLabel"]["@value"]
                associations.append(ass)
                df.at[range, "association"] = associations
            # print(associations)
        print(associations)
    except Exception:
        pass


def safe_value(field_val):
    return field_val if not pd.isna(field_val) else "Other"


