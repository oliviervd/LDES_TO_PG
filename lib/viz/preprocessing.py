import pandas as pd
import matplotlib.pyplot as plt
from lib.parser.parser_im import df_im
from lib.parser.parser_dmg import df_dmg
from lib.parser.parser_hva import df_hva
from lib.parser.parser_stam import df_stam
from lib.parser.parser_agent import df_agents


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




