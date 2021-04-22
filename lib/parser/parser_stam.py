#PARSE DATA FROM JSON TO DATAFRAME

import pandas as pd
from utils import *
import json

df_stam = pd.DataFrame(generate_dataframe("STAM"))

columns = ["URI", "@type", "title ", "provenance", "material", "description", "collection"]
for i in range(0, len(df_stam)):
    df_stam.insert(i, columns[i], "")

for i in range(0, len(df_stam)):
    x = df_stam.loc[i]
    j = json.loads(x[0])

    #URI
    uri, type = j["http://purl.org/dc/terms/isVersionOf"]["@id"], j["@type"]
    df_stam.at[i, "URI"] = uri
    df_stam.at[i, "@yppe"] = type

    fetch_title(df_stam, i, j)
    fetch_provenance(df_stam, i, j)
    fetch_techniek(df_stam, i, j)
    fetch_collection(df_stam, i, j)
    fetch_description(df_stam, i, j)

