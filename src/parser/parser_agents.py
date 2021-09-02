from src.utils.utils import *
import json


def generate_dataframe_AGENTS():
    df_agents = pd.DataFrame(generate_dataframe("AGENT"))

    for i in range(0, len(columns_agents)):
        df_agents.insert(i, columns_agents[i], "")

    for i in range(0, len(df_agents)):
        x = df_agents.loc[i]
        j = json.loads(x[0])

    return df_agents

generate_dataframe_AGENTS()