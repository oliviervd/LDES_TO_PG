#PARSE DATA FROM JSON TO DATAFRAME

import pandas as pd
from utils import *
import json

df_dmg = pd.DataFrame(generate_dataframe("DMG"))

for i in range(0, len(columns)):
    df_dmg.insert(i, columns[i], "")

for i in range(0, len(df_dmg)):
    x = df_dmg.loc[i]
    j = json.loads(x[0])

    # URI
    uri, type = j["http://purl.org/dc/terms/isVersionOf"]["@id"], j["@type"]
    df_dmg.at[i, "URI"] = uri
    df_dmg.at[i, "@type"] = type

    fetch_title(df_dmg, i, j)
    fetch_provenance(df_dmg, i, j)
    # fetch_provenance_date(df_dmg, i, j)
    fetch_techniek(df_dmg, i , j)
    fetch_collection(df_dmg, i, j)
    fetch_description(df_dmg, i, j)





