import pandas as pd
import json
from utils import filepath, generate_dataframe

pd.set_option('display.max_colwidth', None)
#
# df_dmg_obj = pd.DataFrame(res)
# columns = ["URI", "@type", "title", "provenance", "material", "description", "collection"]
# for i in range(0, len(columns)):
#     df_dmg_obj.insert(i, columns[i], "")
#
# for i in range(0, len(df_dmg_obj)):
#     x = df_dmg_obj.loc[i]
#     j = json.loads(x[0])
#
#     ##URI + @type
#     uri, type = j["@id"], j["@type"]
#     df_dmg_obj.at[i, "URI"] = uri
#     df_dmg_obj.at[i, "@type"] = type
#
#     #title
#     try:
#         title = j["http://www.cidoc-crm.org/cidoc-crm/P102_has_title"]
#         df_dmg_obj.at[i, "title"] = title["@value"]
#     except Exception:
#         pass
#
#     #provenance
#     try:
#         prov = j["MaterieelDing.isOvergedragenBijVerwerving"]
#         df_dmg_obj.at[i, "provenance"] = prov
#     except Exception:
#         pass
#
#     #techniek
#     try:
#         material = j["MaterieelDing.bestaatUit"]
#         df_dmg_obj.at[i, "material"] = material
#     except Exception:
#         pass
#
#     #description
#     try:
#         description = j["http://www.cidoc-crm.org/cidoc-crm/P3_has_note"]
#         df_dmg_obj.at[i, "description"] = description["@value"]
#     except Exception:
#         pass
#
#     #collection
#     try:
#         collection = j["MensgemaaktObject.maaktDeelUitVan"]
#         collections = []
#         for x in collection:
#             collections.append(x["Recht.type"])
#         df_dmg_obj.at[i, "collection"] = collections
#     except Exception:
#         pass
#
#     #TODO: maker (+plaats en rol)
#     #TODO: associaties (persoon - onderwerp - geografisch)
#     #TODO: production (datum + precisie)