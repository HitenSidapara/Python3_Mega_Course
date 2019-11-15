import folium
import pandas as pd

# Read The csv File

data = pd.read_csv("in.csv")

lat = list(data["lat"])
lng = list(data["lng"])
population = list(data["population"])


# create the function according to the population change color


def population_color(population):
    if population <= 289429.0:
        return "green"
    elif population >= 289429.0 and population <= 2026000.0:
        return "orange"
    else:
        return "red"


# main map object


map = folium.Map(location=[19.076952, 72.882554], zoom_start=6, tiles="Stamen Terrain")

# First Group

fg = folium.FeatureGroup(name="City Population")

for lat, lng, population in zip(lat, lng, population):
    fg.add_child(folium.CircleMarker(location=[lat, lng], radius=6, popup=str(population),
                                     fill_color=population_color(population), color=population_color(population),
                                     fill_opacity=0.6))

fgg = folium.FeatureGroup(name="Population")

fgg.add_child(folium.GeoJson(open("world.json", 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x:
                             {'fillColor': 'green'
                             if x["properties"]["POP2005"] < 1000000
                             else 'orange'
                             if 1000000 <= x["properties"]['POP2005'] < 2000000
                             else 'red'}))

map.add_child(fg)
map.add_child(fgg)
map.add_child(folium.LayerControl())

map.save("Map.html")
