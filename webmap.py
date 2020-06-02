print("welcome to webmap application")
import folium
import pandas as pd
data = pd.read_csv("data.txt")
Latitude = list(data["LAT"])
Longigute = list(data["LON"])
elevation = list(data["ELEV"])

def color_decider(elevation_value):
    if elevation_value < 1500:
        return "green"
    elif 1500 <= elevation_value < 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.58,-99.09], zoom_start=4.8, tiles = "Stamen Terrain")
print(map)
featuregroupadd = folium.FeatureGroup(name="my First map")
for Lati, Loni, elev in zip(Latitude,Longigute,elevation):
    featuregroupadd.add_child(folium.CircleMarker(location=[Lati, Loni], radius=6, popup=str(elev) + "meter",fill_color=color_decider(elev),color= "blue",fill_opacity=0.7))
    #featuregroupadd.add_child(folium.Marker(location=[Lati, Loni],popup=str(elev) + "meter", icon=folium.Icon(color=color_decider(elev))))

featuregroupadd.add_child(folium.GeoJson(data=open("world.json","r", 
encoding="utf-8-sig"),
style_function=lambda x: {'fillColor':'Yellow' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(featuregroupadd)
map.save("Map1.html")