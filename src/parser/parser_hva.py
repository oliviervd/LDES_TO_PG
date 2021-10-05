#PARSE DATA FROM JSON TO DATAFRAME

import json
from src.utils.utils import *
pd.set_option('display.max_colwidth', None)

def generate_dataframe_hva():
    df_hva = pd.DataFrame(generate_dataframe("HVA"))

    for i in range(0, len(columns_obj)):
        df_hva.insert(i, columns_obj[i], "")

    for i in range(0, len(df_hva)):
        x = df_hva.loc[i]
        j = json.loads(x[0])

        #URI
        uri, type = j["http://purl.org/dc/terms/isVersionOf"]["@id"], j["@type"]
        df_hva.at[i, "URI"] = uri
        df_hva.at[i, "@type"] = type

        fetch_title(df_hva, i, j)
        fetch_owner(df_hva, i, j)
        fetch_objectname(df_hva, i, j)
        fetch_objectnaam_id(df_hva, i, j)
        fetch_provenance(df_hva, i, j)
        fetch_creator(df_hva, i, j)
        fetch_creator_role(df_hva,i ,j)
        fetch_creator_place(df_hva, i, j)
        fetch_creation_date(df_hva, i, j)
        fetch_location(df_hva, i , j)
        fetch_material(df_hva, i , j)
        fetch_collection(df_hva, i, j)
        fetch_description(df_hva, i, j)
        fetch_timestamp(df_hva, i, j)
    return df_hva
#TODO: add to mongoDB