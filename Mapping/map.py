import folium
import pandas
import cv2

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""
def color_Code(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <2000:
        return 'blue'
    else:
        return 'red'


map = folium.Map(zoom_start=6, tiles="OpenStreetMap")
#layercontrol
fq = folium.FeatureGroup(name="My map")

for lt, ln, el in zip(lat, lon, elev):
    fq.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon=folium.Icon(color=color_Code(el))))

map.add_child(fq)

map.save("map2.html")

mydict = ["name","John", "surname","Smith"]

print(mydict)
print('John')
