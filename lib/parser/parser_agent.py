import pandas as pd
from utils.utils import *
import json


def generate_dataframe_AGENTS():
    df_agents = pd.DataFrame(generate_dataframe("AGENTS"))

    for i in range(0, len(columns_agents)):
        df_agents.insert(i, columns_agents[i], "")

