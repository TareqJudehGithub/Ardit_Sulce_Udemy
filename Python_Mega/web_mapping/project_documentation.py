"""
libraries/modules
 1. Live Server.
      Live Server extension for directly opening html files in the default
      browser.

 2. folium 
      folium makes beautiful maps with Python.
      Installation   $ pip install folium
      webpage: https://pypi.org/project/folium/

3.  pandas
     $ pip install pandas

     data = pandas.read_csv("filepath/filename")  
     - pandas data is called DataFrame.

      
"""
import folium as fol

# create a map object
jo_map = fol.Map(
     # latitude and longitude of map
     location=[31.963158, 35.930359], 
     # map starting zoom: default =10
     zoom_start=6,
     # Map tileset to use
     tiles="Stamen Terrain"
     )

coords_1 = [38.2,-99.1]
coords_2 = [38.4,-99.3]
coords = [[38.2,-99.1], [38.4,-99.3]]

# we can setup a Feature Group to make it easier to add markers on map:
fg = fol.FeatureGroup(name="My markers")


# add a single marker on map. Markers allows text pop-ups on map.
fg.add_child(
     fol.Marker(location=[], 
          popup="text",
          icon=fol.Icon(color="pick a color")
          )
     )

# or add multiple using Feature Group
for coord in coords:
     fg.add_child(
          fol.Marker(
               location=[coord],
               popup="marker",
               icon=fol.Icon(color="green")
          )
     )

jo_map.add_child(fg)

# save map as html file
jo_map.save("JO_map.html")

