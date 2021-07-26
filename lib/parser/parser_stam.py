#PARSE DATA FROM JSON TO DATAFRAME

import pandas as pd
from utils.utils import *
import json

def generate_dataframe_stam():

    df_stam = pd.DataFrame(generate_dataframe("STAM"))

    for i in range(0, len(columns_obj)):
        df_stam.insert(i, columns_obj[i], "")

    for i in range(0, len(df_stam)):
        x = df_stam.loc[i]
        j = json.loads(x[0])

        #URI
        uri, type = j["http://purl.org/dc/terms/isVersionOf"]["@id"], j["@type"]
        df_stam.at[i, "URI"] = uri
        df_stam.at[i, "@yppe"] = type

        fetch_title(df_stam, i, j)
        fetch_owner(df_stam, i, j)
        fetch_objectname(df_stam, i, j)
        fetch_provenance(df_stam, i, j)
        fetch_creator(df_stam, i, j)
        fetch_creator_role(df_stam,i ,j)
        fetch_creator_place(df_stam, i, j)
        #fetch_provenance_date(df_stam, i, j)
        fetch_material(df_stam, i , j)
        fetch_material_source(df_stam, i , j)
        fetch_location(df_stam, i , j)
        fetch_collection(df_stam, i, j)
        fetch_description(df_stam, i, j)
        fetch_timestamp(df_stam, i, j)
    return df_stam
#TODO: add to ES

