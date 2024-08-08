import pandas as pd
import plotly.express as px

venue = pd.read_excel("../data/raw/Paris 2024 Venue Locations.xlsx")


fig = px.scatter_mapbox(
    venue,
    lat="latitude",
    lon="longitude",
    hover_data=["location", "Nom_Site", "Sports"],
    color_discrete_sequence=["#1b263b"],
    zoom=3,
    height=300,
)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
