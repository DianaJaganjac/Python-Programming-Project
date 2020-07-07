# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:13:53 2019
@author: Diana Jaganjac
"""
import random as rand
from sys import maxsize
import copy
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
import math



def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 
      [(state, city, latitude, longitude), ...] 
    Use this as your initial `road_map`, that is, the cycle 
      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    f = open(file_name)
    lines = f.readlines()
    result = []
    for line in lines:
        line = line.strip("\n")
        ele = line.split("\t")
        joinele = (ele[0]), (ele[1]), float(ele[2]), float(ele[3])
        result.append(joinele)
    return (result)
    f.close
    
z = read_cities(r"city-data.txt")
#print(z)
  
def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    result = []
    for ele in road_map:
        rm = ((ele[1]), (round(ele[2],1)), (round(ele[3],1)))
        result.append(rm)        
    return result


road_map = print_cities(z)
#print(road_map)

def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    coords = []
    for i in road_map:
        coords.append(i[1])
        coords.append(i[2])
        
    x = [float(r) for r in coords[0::2]]
    y = [float(r) for r in coords[1::2]]
    
    xy = list(zip(x,y))
    
    dist = 0
    
    for r in range(len(xy)-1):
        dist += math.sqrt((xy[r][0]-xy[r+1][0])**2 + (xy[r][1]-xy[r+1][1])**2)
    
    return round(dist, 1)

#d = compute_total_distance(new_road_map)
#print(d)

def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index1` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 
        (new_road_map, new_total_distance)
    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    new_road_map = copy.deepcopy(road_map)
    
    if index1 != index2:
        position = new_road_map[index1], new_road_map[index2]
        new_road_map[index2], new_road_map[index1] = position
        
    if index1 == index2:
        pass

    new_total_distance = compute_total_distance(new_road_map)
    
    return (new_road_map, new_total_distance)
   
#h = swap_cities(road_map, 0, 4)
#print(h)
        
def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """

    road_map.insert(0, road_map.pop())
    new_dist = compute_total_distance(road_map)
    return (road_map, new_dist)

#g = shift_cities(new_road_map)
#print(g)
    
def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """  
    shortest_dist = maxsize
    best_cycle = road_map
    
    for n in range(0, 10000):
        
        number1 = rand.randint(0,(len(road_map)-1))
        number2 = rand.randint(0,(len(road_map)-1))
        
        (cycle1, dist_1) = swap_cities(best_cycle, number1, number2)
        
        if dist_1 < shortest_dist:
            shortest_dist = dist_1
            best_cycle = cycle1
            
        (cycle2, dist_2) = shift_cities(best_cycle)
        
        if dist_2 < shortest_dist:
            shortest_dist = dist_2
            best_cycle = cycle2
            
    return best_cycle

s = find_best_cycle(road_map)
print(s)
#alist = []
#for i in range(10):
#    s = find_best_cycle(road_map)
#    alist.append(s)
#print(alist)
   
        
def distance_cities(road_map):
    
    coords = []
    ind = []
    for i in road_map:
        coords.append(i[1])
        coords.append(i[2])
        
    x = [float(r) for r in coords[0::2]]
    y = [float(r) for r in coords[1::2]]
    
    xy = list(zip(x,y))
    
    for r in range(len(xy)-1):
        dist = math.sqrt((xy[r][0]-xy[r+1][0])**2 + (xy[r][1]-xy[r+1][1])**2)
        rounded = round(dist, 1)
        ind.append(rounded)
        
    return ind

    
#k = distance_cities(road_map)
#print(k)       


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    cities = find_best_cycle(road_map)
    cost = distance_cities(cities)
    
    for i in range(len(cities)-1):
         indc = cost[i]
         endvar = f"The cost from {cities[i][0]} to {cities[i+1][0]} is {indc}."
         print(endvar)
         
    total_cost = compute_total_distance(road_map)
    total = f"The total cost is {total_cost}"
    
    return total

#c = print_map(road_map)
#print(c)
  

def main(file_name):
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
 
    if __name__ == "__main__": #keep this in
        
        file = read_cities(file_name)
        road_map = print_cities(file)
        print()
        
        result = find_best_cycle(road_map)
        result.append(result[0])
        total_cost = compute_total_distance(result)
        
        return f"The best cycle is {result} with a total cost of {total_cost}"
        
final = main(r"city-data.txt")
print(final)
        
def visualise(road_map):
    fp = (r"states.shp")
    map_df = gpd.read_file(fp)
    
    df = pd.read_csv(r"city-data.csv", header=0)
    merged = map_df.set_index("STATE_NAME").join(df.set_index("State"))
    data = merged.drop(["District of Columbia"])
    
    geometry = [Point(xy) for xy in zip(data["Long"], data["Lat"])]
    geo_df = gpd.GeoDataFrame(data, geometry = geometry)
   
    dots = []
    d = find_best_cycle(road_map)
    d.append(d[0])
    
    for i in d:
        dots.append(i[1])
        dots.append(i[2])
    
    x = [float(r) for r in dots[0::2]]
    y = [float(r) for r in dots[1::2]]
    xy = list(zip(y,x))
    
    n = []
    count = 0
    for i in xy:
        count +=1
        n.append(count)
    n.remove(n[-1])

    start = [Point(xy[0])]
    start_df = gpd.GeoDataFrame(geometry = start)

    line = [LineString(xy)]
    line_df = gpd.GeoDataFrame(geometry = line)
    line_df.to_file("line.shp")
    
    route = (r"line.shp")
    route_df = gpd.read_file(route)
    route_df.crs = ({'init': 'epsg:4269'})

    fig, ax = plt.subplots(figsize=(28, 12))
    map_df.plot(ax=ax)
    geo_df.plot(ax = ax, markersize = 10, color = "red", marker = "o", label = "US Capital Cities")
    start_df.plot(ax = ax, marker = "*", color = "yellow", markersize = 20, label = "Starting Point")
    route_df.plot(ax = ax, linewidth = 1, color = "orange", label = "Route Map")
    for i, txt in enumerate(n):
        ax.annotate(txt, (xy[i]), fontsize = 8)
    plt.legend()
    plt.title("Travelling Salesman Solution")
    
    return ax


d = visualise(road_map)
print(d)
