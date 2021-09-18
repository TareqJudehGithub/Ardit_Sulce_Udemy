from datetime import date
import folium as fol
from folium.map import Icon, Marker
import pandas

# create new map object
web_map = fol.Map(
  location=[38.58, -99.09],
  tiles="Stamen Terrain",
  zoom_start=0
)

# extract latitude, longitude and elevation using pandas
data = pandas.read_csv("./files/Volcanoes.txt")
lati = data["LAT"]
long =data["LON"]
elev = data["ELEV"]
volc = data["NAME"]

# marker color based on elevation
def color_producer(elevation):
  if elevation < 1000:
    return "green"
  elif 1000 <= elevation <= 2000:
    return "orange"
  else:
    return "red"


# feature group for markers
fg = fol.FeatureGroup(name="My Map")

# combine lat and long in one list 
lati_long_elev = list(zip(lati, long, volc, elev))

# point layers setup:
for lat, lon, vol, ele in lati_long_elev:
  fg.add_child(

    # fol.Marker(
    #   location=[lat, lon],
    #   popup=f"{ele} ft",
    #   tooltip=vol, 
    #   icon=fol.Icon(color=color_producer(ele))
    # )
    (
      fol.CircleMarker(
        location=[lat, lon],
        popup=f"{ele} ft",
        tooltip=vol,
        radius=6,
        fill_color=color_producer(ele),
        color="grey",
        fill=True,
        fill_opacity=0.7
      )
    )
  )

# polygon setup (adding borders to each country):
population = lambda x: {
  "fillColor": "green" if x["properties"]["POP2005"] < 10000000
  else "orange" if 10000000 >= x["properties"]["POP2005"] < 20000000
  else "red"
}

fg.add_child(
  fol.GeoJson(
    data=open('./files/world.json', mode="r", encoding="utf-8-sig").read(),
    style_function=population

    )
)

# # add marker(s) to map
web_map.add_child(fg)

# # save to html file
web_map.save("web_map.html")
