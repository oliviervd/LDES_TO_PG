import pandas as pd
from skosprovider_getty.providers import AATProvider
import numpy as np
import regex as re
from lib.viz.json_to_pg import df_all

thes_1 = df_all.explode("object_name_id").fillna(0)
df_on_trans = thes_1["object_name_id"]
df_on_trans = df_on_trans.drop_duplicates()

aat = AATProvider(metadata={"id" : "AAT"})
lang = ["en", "nl", "fr", "it", "de", "es"]

df_translation = pd.DataFrame(columns=lang)
## TODO: create index based on PID
x = df_on_trans["id"] = df_on_trans.str.rsplit("/", 1)
for id in x:
    try:
        AAT_term = id[-1]
        # print(AAT_term)
        hash = aat.get_by_id(AAT_term)
        l_temp = []
        # l_temp.append(AAT_term)
        print("Label per language")
        print("------------------")
        for l in lang:
            label = hash.label(l)
            if hash.label(l).language == l:
                l_temp.append(label.label)
                print(l + ' --> ' + label.language + ': ' + label.label + ' [' + label.type + ']')
            else:
                l_temp.append("-")

        numEl = len(l_temp)
        newRow = pd.DataFrame(np.array(l_temp).reshape(1, numEl),
                            columns=list(df_translation.columns))
        df_translation = df_translation.append(newRow)
        # print(l_temp)

    except:
        print("invalid ID")

df_translation.to_csv("objectname_translations.csv")