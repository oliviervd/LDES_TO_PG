import pandas as pd
import matplotlib.pyplot as plt
from lib.parser.parser_im import generate_dataframe_im
from lib.parser.parser_dmg import generate_dataframe_DMG
from lib.parser.parser_hva import generate_dataframe_hva
from lib.parser.parser_stam import generate_dataframe_stam
from lib.parser.parser_agent import df_agents

df_im = generate_dataframe_im()
df_stam = generate_dataframe_stam()
df_dmg = generate_dataframe_DMG()
df_hva = generate_dataframe_hva()

df_all = pd.concat([df_dmg, df_im, df_hva, df_stam])


# df.pivot_table(['int_age'],index = [df.iloc[:,meet_friends], df.iloc[:,friendsgiving]])

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
        total = count_im + count_dmg + count_hva + count_stam

        data = {
            "INST": ["STAM", "Design Museum Gent", "Huis van Alijn", "Industriemuseum"],
            "object_count": [count_stam, count_dmg, count_hva, count_im]
        }

        df_count = pd.DataFrame(data, columns=["INST", "object_count"])
        return df_count

    except Exception:
        pass



