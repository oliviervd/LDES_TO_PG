import plotly.express as px

def main_counter():
    """countdown to 100.000 objects"""
    z = [75000] ##temp
    fig = px.bar(z, x="total number of objects already published", orientation="h")
    fig.show()
