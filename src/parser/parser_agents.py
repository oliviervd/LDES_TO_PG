from src.utils.utils import *
import json


def generate_dataframe_AGENTS():
    df_agents = pd.DataFrame(generate_dataframe("AGENT"))

    for i in range(0, len(columns_agents)):
        df_agents.insert(i, columns_agents[i], "")

    for i in range(0, len(df_agents)):
        x = df_agents.loc[i]
        j = json.loads(x[0])

        uri, type = j["@id"], j["@type"]
        df_agents.at[i, "URI"] = uri
        df_agents.at[i, "@type"] = type

        fetch_agent_fullname(df_agents, i, j)
        fetch_agent_family_name(df_agents, i, j)

    return df_agents

generate_dataframe_AGENTS()