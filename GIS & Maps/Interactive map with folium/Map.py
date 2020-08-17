# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:46:13 2019

@author: jeafreezy
"""

#THIS CODE CREATES AN INTERACTIVE MAP FOR ANY PURPOSE
#Importing the libraries
import pandas as pd
import folium
#importing the dataset
dataset=pd.read_csv(file_path)
locations=dataset[['Latitude','Longitude']]
tag=dataset['NAME']
bts=locations.values.tolist()

#Initializing Empty Map,Zoomed In to  Center
Center_Coordinates=(7.127799996,3.2780999960000003)
map=folium.Map(location=Center_Coordinates,zoom_start=12,tiles='CartoDBPositron')
tooltip='Click Me!'
#Creating Markers for each locations
for points,tags in zip(bts,tag):
               map.add_child(folium.Marker(location=points,
               popup=tags,icon=folium.Icon(color='green',icon='info-sign')))
               print(points,tags)
      #Creating a buffer of 50m round each points
        for circle in points:
           folium.CircleMarker(location=[45.5215, -122.6261],
                    radius=50,
                    popup='Laurelhurst Park',
                    color='#3186cc',
                    fill=True,
                    fill_color='#3186cc'
                    ).add_to(map)
            #export code as HTML 
map.save("./mymap.html")

