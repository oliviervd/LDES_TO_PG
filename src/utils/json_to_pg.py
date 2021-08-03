import pandas as pd
from sqlalchemy import create_engine

from src.parser.parser_im import generate_dataframe_im
from src.parser.parser_dmg import generate_dataframe_DMG
from src.parser.parser_hva import generate_dataframe_hva
from src.parser.parser_stam import generate_dataframe_stam
from src.parser.parser_thes import generate_dataframe_thesaurus
from src.parser.parser_agents import generate_dataframe_AGENTS

# from src.parser.parser_archief import

df_im = generate_dataframe_im()
df_stam = generate_dataframe_stam()
df_dmg = generate_dataframe_DMG()
df_hva = generate_dataframe_hva()
# df_archief = generate_dataframe_archief()
df_thes = generate_dataframe_thesaurus()
df_agents = generate_dataframe_AGENTS()
df_all = pd.concat([df_dmg, df_im, df_hva, df_stam])

post_gres_credentials = "postgresql://postgres:co2etzee1648@localhost:5432/postgres"
engine = create_engine(post_gres_credentials)
# df_dmg.to_sql('ldes_dmg', engine)
# df_stam.to_sql("ldes_stam", engine)
# df_im.to_sql("ldes_im", engine)
# df_hva.to_sql("ldes_hva", engine)


def object_counter():
    try:
        count_stam = len(df_stam["URI"])
        count_dmg = len(df_dmg["URI"])
        count_hva = len(df_hva["URI"])
        count_im = len(df_im["URI"])
        total = count_im + count_dmg + count_hva + count_stam
        return total
    except Exception:
        pass


def general_tracker():
    try:
        count_stam = len(df_stam["URI"])
        count_dmg = len(df_dmg["URI"])
        count_hva = len(df_hva["URI"])
        count_im = len(df_im["URI"])

        data = {
            "INST": ["STAM", "Design Museum Gent", "Huis van Alijn", "Industriemuseum"],
            "object_count": [count_stam, count_dmg, count_hva, count_im]
        }

        df_count = pd.DataFrame(data, columns=["INST", "object_count"])
        return df_count

    except Exception:
        pass


df_dmg_final_len = len(df_dmg.URI.unique())
df_hva_final_len = len(df_hva.URI.unique())
df_im_final_len = len(df_im.URI.unique())
df_stam_final_len = len(df_stam.URI.unique())

# df_dmg_final = df_dmg.groupby(["URI"], sort=False)["timestamp"].max()
df_dmg_final = df_dmg.groupby(["URI"], sort=False, as_index=False)["timestamp"].max()
# df_d_final = pd.merge(df_dmg, df_dmg_final_2, how='left', left_on=["URI", "timestamp"], right_on=["URI", "timestamp"])
