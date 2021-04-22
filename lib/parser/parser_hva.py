#PARSE DATA FROM JSON TO DATAFRAME

import json
import pandas as pd
from utils import *
pd.set_option('display.max_colwidth', None)

df_hva = pd.DataFrame(generate_dataframe("HVA"))

columns = ["URI", "@type", "title", "provenance", "material", "description", "collection"]
for i in range(0, len(columns)):
    df_hva.insert(i, columns[i], "")

for i in range(0, len(df_hva)):
    x = df_hva.loc[i]
    j = json.loads(x[0])

    #URI
    uri, type = j["@id"], j["@type"]
    df_hva.at[i, "URI"] = uri
    df_hva.at[i, "@type"] = type

    fetch_title(df_hva,i ,j)
    fetch_provenance(df_hva, i, j)
    fetch_techniek(df_hva, i, j)
    fetch_collection(df_hva, i, j)
    fetch_description(df_hva, i, j)