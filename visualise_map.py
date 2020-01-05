# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:43:06 2020

@author: Diana Jaganjac
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString

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

lines = [xy for xy in zip(round(data["long"], data["lat"]),2)]
#lines_df = gpd.GeoDataFrame(data, lines = lines)
print(lines)
#
#
#fig, ax = plt.subplots(figsize=(14, 6))
#map_df.plot(ax=ax)
#geo_df.plot(ax = ax, markersize = 10, color = "red", marker = "o")
#lines_df.plot(ax = ax, color = "orange")



