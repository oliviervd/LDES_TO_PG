#PARSE DATA FROM JSON TO DATAFRAME

import pandas as pd
from utils import *
import json

df_im = pd.DataFrame(generate_dataframe("IM"))

columns = ["URI", "@type", "title", "provenance", "material", "description", "collection"]
for i in range(0, len(columns)):
    df_im.insert(i, columns[i], "")

for i in range(0, len(df_im)):
    x = df_im.loc[i]
    j = json.loads(x[0])

    # URI
    uri, type = j["http://purl.org/dc/terms/isVersionOf"]["@id"], j["@type"]
    df_im.at[i, "URI"] = uri
    df_im.at[i, "@type"] = type

    fetch_title(df_im, i, j)
    fetch_provenance(df_im, i, j)
    fetch_techniek(df_im, i, j)
    fetch_collection(df_im, i, j)
    fetch_description(df_im, i, j)