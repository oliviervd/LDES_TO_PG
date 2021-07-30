## parse data from JSON-LD to DF to populate Postgres

from src.utils.utils import *
import json

def generate_dataframe_THES():
    df_thes = pd.DataFrame(generate_dataframe("THES"))

    for i in range(0, len(columns_thes)):
        df_thes.insert(i, columns_thes[i], "")

    for i in range(0, len(df_thes)):
        x = df_thes.loc[i]
        j = json.loads(x[0])
        # print(j["http://purl.org/dc/terms/isVersionOf"])

        uri = j["http://purl.org/dc/terms/isVersionOf"]
        df_thes.at[i, "URI"] = uri

        fetch_timestamp(df_thes, i, j)
        fetch_thes_term(df_thes, i, j)
        fetch_thes_ext_URI(df_thes, i, j)



    return df_thes

