#PARSE DATA FROM JSON TO DATAFRAME

import pandas as pd
from utils.utils import *
import json

def generate_dataframe_DMG():
    df_dmg = pd.DataFrame(generate_dataframe("DMG"))

    for i in range(0, len(columns_obj)):
        df_dmg.insert(i, columns_obj[i], "")

    for i in range(0, len(df_dmg)):
        x = df_dmg.loc[i]
        j = json.loads(x[0])

        # URI
        uri, type = j["http://purl.org/dc/terms/isVersionOf"]["@id"], j["@type"]
        df_dmg.at[i, "URI"] = uri
        df_dmg.at[i, "@type"] = type

        fetch_title(df_dmg, i, j)

        fetch_objectnumber(df_dmg, i, j)

        fetch_owner(df_dmg, i, j)
        fetch_location(df_dmg, i, j)

        fetch_objectname(df_dmg, i, j)
        fetch_objectnaam_id(df_dmg, i, j)

        fetch_provenance(df_dmg, i, j)

        fetch_creator(df_dmg, i, j)
        fetch_creation_date(df_dmg, i, j)
        fetch_creator_role(df_dmg,i ,j)
        fetch_creator_place(df_dmg, i, j)

        fetch_material(df_dmg, i , j)

        fetch_collection(df_dmg, i, j)
        fetch_description(df_dmg, i, j)
        fetch_timestamp(df_dmg, i, j)

    return df_dmg






