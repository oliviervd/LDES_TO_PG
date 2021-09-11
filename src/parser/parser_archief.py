from src.utils.utils import *
import json
import pandas as pd

def generate_dataframe_ARCH():
    df_archief = pd.DataFrame(generate_dataframe("ARCH"))

    for i in range(0, len(columns_obj)):
        df_archief.insert(i, columns_obj[i], "")

    for i in range(0, len(df_archief)):
        x = df_archief.loc[i]
        j = json.loads(x[0])

        #uri
        uri, type = j["http://purl.org/dc/terms/isVersionOf"]["@id"], j["@type"]
        df_archief.at[i, "URI"] = uri
        df_archief.at[i, "@type"] = type

        fetch_title(df_archief, i, j)
        fetch_owner(df_archief, i, j)
        fetch_objectname(df_archief, i, j)
        fetch_provenance(df_archief, i, j)

        fetch_creator(df_archief, i, j)
        fetch_creator_role(df_archief, i, j)
        fetch_creator_place(df_archief, i, j)
        fetch_creation_date(df_archief, i, j)

        fetch_material(df_archief, i , j)
        fetch_location(df_archief, i , j)
        fetch_collection(df_archief, i, j)
        fetch_description(df_archief, i, j)
        fetch_timestamp(df_archief, i, j)

    return df_archief
