import plotly.express as px
from lib.viz.preprocessing import general_tracker
from lib.viz.preprocessing import df_all

##general counter
df_c = general_tracker()
fig = px.bar(df_c, x="object_count", y="INST", orientation="h")
fig.show()

##object_name grouped by institution
def object_name_grp_collection():
    """"create new frame with exploded object_names"""
    df_obj_piv = df_all.explode("object_name")
    fig = px.bar(df_obj_piv, x="object_name", orientation="h", color="owner")
    fig.show()

