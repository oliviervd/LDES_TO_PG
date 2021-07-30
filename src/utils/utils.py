import time
import subprocess
import pandas as pd

today = time.localtime()
time_str = time.strftime("%m-%d-%YT%H:%M:%S.309Z", today)

# define time from when to start fetching LDES.
fetch_from = "2021-01-01T15:48:12.309Z"
context = "src/utils/context.jsonld"

endpoints = {
    # CLI commands to fetch LDES from actor-init-ldes-client
    "DMG": f"actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
            f"" + context + " --fromTime " + fetch_from + " --emitMemberOnce true --disablePolling true"
            f" https://apidg.gent.be/opendata/adlib2eventstream/v1/dmg/objecten",
    "HVA": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
            + context + " --fromTime " + fetch_from + " --emitMemberOnce true --disablePolling true"
            " https://apidg.gent.be/opendata/adlib2eventstream/v1/hva/objecten",
    "STAM": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
            + context + "  --fromTime " + fetch_from + " --emitMemberOnce true --disablePolling true"
            " https://apidg.gent.be/opendata/adlib2eventstream/v1/stam/objecten",
    "IM": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
            + context + "   --fromTime " + fetch_from + " --emitMemberOnce true --disablePolling true"
            " https://apidg.gent.be/opendata/adlib2eventstream/v1/industriemuseum/objecten",
    "ARCH": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
            + context + "   --fromTime  "+ fetch_from +" --emitMemberOnce true --disablePolling true"
            " https://apidg.gent.be/opendata/adlib2eventstream/v1/archiefgent/objecten",
    "THES": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
            + context + "   --fromTime "+ fetch_from + " --emitMemberOnce true --disablePolling true"
            " https://apidg.gent.be/opendata/adlib2eventstream/v1/adlib/thesaurus",
    "AGENT": "actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context "
            +  context + "  --fromTime " + fetch_from + " --emitMemberOnce true --disablePolling true"
            " https://apidg.gent.be/opendata/adlib2eventstream/v1/adlib/personen"
}

print(endpoints)

filepath = {
    "DMG": "data/dmg_obj.json",
    "HVA": "data/hva_obj.json",
    "STAM": "data/stam_obj.json",
    "IM": "data/im_obj.json",
    "ARCH": "data/arch_obj.json",
    "THES": "data/thes.json",
    "AGENT": "data/agents.json"
}

# todo: add function to generat json files and data directory if not already created
# todo: fetch techniek
# todo: add argparse


# define columns to for dataframes
columns_obj = ["URI", "timestamp", "@type", "owner", "objectnumber", "title", "object_name", "object_name_id",
               "creator", "creator_role", "creation_date", "creation_place","provenance_date", "provenance_type",
               "material", "material_source", "description", "collection", "association", "location"]

columns_thes = ["URI", "timestamp", "term", "ext_URI"]

columns_agents = ["URI", "timestamp", "full name", "family_name", "sirname", "name (organisations)", "date_of_birt",
                  "date_of_death", "place of birt", "place of death", "nationality", "gender", "same_as"]


def fetch_json(key):
    """read json from command line interface and write to .json file"""
    with open(filepath[key], "w") as f:
        p = subprocess.run(endpoints[key], shell=True, stdout=f, text=True)


def generate_dataframe(key):
    with open(filepath[key]) as p:
        res = p.read()
        res = res.splitlines()
        print("Done with parsing data from {}".format(key))
        # print("Done with parsing data from {}".format(key))
        return res


def fetch_objectnumber(df, range, json):
    """parse object number from json"""
    try:
        object_number = json["Object.identificator"]["Identificator.identificator"]
        df.at[range, "objectnumber"] = object_number
    except Exception:
        pass


def fetch_owner(df, range, json):
    """parse object owner from json"""
    try:
        owner = json["MaterieelDing.beheerder"]
        df.at[range, "owner"] = owner
    except Exception:
        pass


def fetch_provenance(df, range, json):
    """fetch provenance dates and transaction method from json"""
    try:
        provenance = json["MaterieelDing.isOvergedragenBijVerwerving"]
        # df.at[range_, "provenance"] = prov
        for x in provenance:
            try:
                prov_date = x["Conditie.periode"]["Periode.einde"]
                df.at[range, "provenance_date"] = prov_date
            except Exception:
                pass
        for x in provenance:
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


def fetch_title(df, range, json):
    """parse object title (dutch) from json"""
    try:
        title = json["http://www.cidoc-crm.org/cidoc-crm/P102_has_title"]
        df.at[range, "title"] = title["@value"]
    except Exception:
        pass


def fetch_material(df, range, json):
    ## fetch material + material source (AAT)
    try:
        material = json["MaterieelDing.bestaatUit"]
        materials = []
        materials_source = []
        for m in material:
            materials.append(m["MensgemaaktObject.materiaal"]["skos:prefLabel"]["@value"])
            materials_source.append(m["MensgemaaktObject.materiaal"]["@id"])
        df.at[range, "material"] = materials
        df.at[range, "material_source"] = materials_source
    except Exception as e:
        pass

def fetch_collection(df, range, json):
    """fetch (internal) collection to which the object belongs"""
    try:
        collection = json["MensgemaaktObject.maaktDeelUitVan"]
        collections = []
        for x in collection:
            c = x["Recht.type"]
            for col in c:
                collections.append(col["http://www.w3.org/2000/01/rdf-schema#label"]["@value"])
        df.at[range, "collection"] = collections
    except Exception as e:
        pass


def fetch_description(df, range, json):
    """fetch description (dutch)"""
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


def fetch_creator(df, range, json):
    creators = []
    try:
        creator = json["MaterieelDing.productie"]["Activiteit.uitgevoerdDoor"]
        for c in creator:
            creators.append(c["http://www.w3.org/2000/01/rdf-schema#label"]["@value"])
        df.at[range, "creator"] = creators
    except Exception:
        try:
            for i in json["MaterieelDing.productie"]:
                cr = i["Activiteit.uitgevoerdDoor"]
                for a in cr:
                    crea = a["http://www.w3.org/2000/01/rdf-schema#label"]["@value"]
                    creators.append(crea)
                    df.at[range, "creator"] = creators
        except Exception:
            pass


def fetch_creator_role(df, range, json):
    creator_role = []
    try:
        role = json["MaterieelDing.productie"]["@type"]
        creator_role.append(role)
        df.at[range, "creator_role"] = creator_role
    except Exception:
        try:
            for i in json["MaterieelDing.productie"]:
                role = i["@type"]
                creator_role.append(role)
                df.at[range, "creator_role"] = creator_role
        except Exception:
            pass


def fetch_creator_place(df, range, json):
    ## todo: fix not parsing multiple lines
    creator_place = []
    try:
        for p in json["MaterieelDing.productie"]["Gebeurtenis.plaats"]:
            place = p["skos:prefLabel"]["@value"]
            creator_place.append(place)
        df.at[range, "creation_place"] = creator_place
    except Exception:
        try:
            for p in json["MaterieelDing.productie"]:
                try:
                    places = p["Gebeurtenis.plaats"]
                    for place in places:
                        cp = place["skos:prefLabel"]["@value"]
                        creator_place.append(cp)
                except Exception:
                    pass
            df.at[range, "creation_place"] = creator_place

        except Exception:
            pass


def fetch_creation_date(df, range, json):
    creation_date = []
    try:
        i = json["MaterieelDing.productie"]["http://www.cidoc-crm.org/cidoc-crm/P4_has_time-span"]["@value"]
        creation_date.append(i)
        df.at[range, "creation_date"] = creation_date
    except Exception:
        try:
            for i in json["MaterieelDing.productie"]:
                try:
                    time = i["http://www.cidoc-crm.org/cidoc-crm/P4_has_time-span"]["@value"]
                    creation_date.append(time)
                except Exception:
                    pass
            df.at[range, "creation_date"] = creation_date
        except Exception:
            pass


def fetch_objectname(df, range, json):
    try:
        object_names = []
        # object_names.append(json["Entiteit.classificatie"])
        try:
            for i in json["Entiteit.classificatie"]:
                for a in i["Classificatie.toegekendType"]:
                    on = a["skos:prefLabel"]["@value"]
                    object_names.append(on)
                    df.at[range, "object_name"] = object_names
        except Exception:
            pass
    except Exception:
        pass

#TODO: classificatie.id (link naar auhtority)
def fetch_objectnaam_id(df, range, json):
    try:
        object_names_auth = []
        try:
            for i in json["Entiteit.classificatie"]:
                for a in i["Classificatie.toegekendType"]:
                    oi = a["@id"]
                    object_names_auth.append(oi)
                    df.at[range, "object_name_id"] = object_names_auth
        except Exception:
            pass
    except Exception:
        pass


def fetch_association(df, range_, json):
    """fetch associated terms related to the object from json"""
    try:
        associations = []
        for i in json["MensgemaaktObject.draagt"]:
            for a in i["Werk.gaatOver"]:
                ass = a["skos:prefLabel"]["@value"]
                associations.append(ass)
                df.at[range_, "association"] = associations
            # print(associations)
        print(associations)
    except Exception:
        pass


def fetch_location(df, range, json):
    """fetch location where the object is currently located from json"""
    try:
       location = json["MensgemaaktObject.locatie"]["http://www.w3.org/2004/02/skos/core#note"]
       df.at[range, "location"] = location
    except Exception:
        pass


def fetch_thesaurus_term(df, range, json):
    """fetch thesaurus label from json"""
    try:
        term = json["http://www.w3.org/2004/02/skos/core#prefLabel"]["@value"]
        df.at[range, "term"] = term
    except Exception:
        pass


def fetch_thesaurus_external_uri(df, range, json):
    """fetch uri refering to the same term from authorised vocabulary such as AAT or Wikidata from json file"""
    try:
        URI = json["http://www.w3.org/2002/07/owl#sameAs"]
        df.at[range, "ext_URI"] = URI
    except Exception:
        pass


def safe_value(field_val):
    return field_val if not pd.isna(field_val) else "Other"
