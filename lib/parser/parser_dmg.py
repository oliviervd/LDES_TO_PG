import pandas as pd
from utils import *
import json

df_dmg = pd.DataFrame(generate_dataframe("DMG"))

columns = ["URI", "@type", "title", "provenance", "material", "description", "collection"]
for i in range(0, len(columns)):
    df_dmg.insert(i, columns[i], "")

for i in range(0, len(df_dmg)):
    x = df_dmg.loc[i]
    j = json.loads(x[0])

    # URI
    uri, type = j["@id"], j["@type"]
    df_dmg.at[i, "URI"] = uri
    df_dmg.at[i, "@type"] = type



