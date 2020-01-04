# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:43:06 2020

@author: Diana Jaganjac
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon 

fp = (r"C:\Users\Diana Jaganjac\pop-one-project-djagan01\states_21basic\states.shp")
map_df = gpd.read_file(fp)

df = pd.read_csv(r"C:\Users\Diana Jaganjac\pop-one-project-djagan01\city-data.csv", header=0)
data_for_map = df.rename(index=str, columns={"State": "state", "City": "city", "Lat": "lat", "Long":"long"})
merged = map_df.set_index("STATE_NAME").join(data_for_map.set_index("state"))
data = merged.drop(["District of Columbia"])
#print(data.head())

geometry = [Point(xy) for xy in zip(data["long"], data["lat"])]

geo_df = gpd.GeoDataFrame(data, geometry = geometry)
#print(geo_df.head())

fig, ax = plt.subplots(figsize=(14, 6))
#var = "city"
#data.plot(column = var, ax=ax)
map_df.plot(ax=ax)
geo_df.plot(ax = ax, markersize = 10, color = "red", marker = "o")


#coords = pd.read_csv(r"C:\Users\Diana Jaganjac\pop-one-project-djagan01\cities_coordinates.csv", header = 0)

