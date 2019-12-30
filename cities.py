# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:13:53 2019

@author: Diana Jaganjac
"""
import random as rand

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
    result.append(result[0])
    return (result)
    f.close
    
#z = read_cities(r"C:\Users\Diana Jaganjac\pop-one-project-djagan01\city-data.txt")
#print(z)
  
def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    result = []
    for ele in road_map:
        rm = ((ele[1]), (round(ele[2],2)), (round(ele[3],2)))
        result.append(rm)        
    return result


#road_map = print_cities(z)
#print(road_map)
    

def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    import math
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
    
    return round(dist, 2)
    
    
#d = compute_total_distance(road_map)
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
    first_ele = road_map.pop(index1)
    sec_ele = road_map.pop(index2-1)
    
    road_map.insert(index1, sec_ele)
    road_map.insert(index2, first_ele)
    
    if index1 == index2:
        pass
    
    import math
    coords = []
    for i in road_map:
        coords.append(i[1])
        coords.append(i[2])
        
    x = [float(r) for r in coords[0::2]]
    y = [float(r) for r in coords[1::2]]
    
    xy = list(zip(x,y))
    
    dist = 0
    
    for r in range(len(xy)-1):
        dist += math.sqrt((xy[r][0]-xy[r+1][0])**2 + (xy[r][1]-xy[r+1][1])**2 )
    
    return (road_map, dist)
   

#n = swap_cities(road_map, 0, 3)
#print(n)
        
def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
        
    road_map.insert(0, road_map.pop())
    return road_map

#for i in range(5):   
#    g = shift_cities(road_map)
#    print(g)
    
def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    number = rand.randint(0,(len(road_map)-1))
    best_cycle_1 = 20000000
    best_cycle_2 = 20000000
    current_cycle_1 = 0
    current_cycle_2 = 0
    
    for i in range(10000):
        
        roadmap1 = swap_cities(road_map, number, number)
        current_cycle_1 = compute_total_distance(road_map)
        if current_cycle_1 < best_cycle_1:
            best_cycle_1 = current_cycle_1
    
        roadmap2 = shift_cities(road_map)
        current_cycle_2 = compute_total_distance(road_map)
        if current_cycle_2 < best_cycle_2:
            best_cycle_2 = current_cycle_2
    
    if best_cycle_1 < best_cycle_2:
        return roadmap1
    else:
        return roadmap2

#alist = []
#for i in range(51):
#    s = find_best_cycle(road_map)
#    alist.append(s)
#print(alist)     
        
def distance_cities(road_map):
    import math
    
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
        rounded = round(dist, 2)
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
    cities = []
    
    for i in road_map:
        cities.append(i[0])
    
    cost = distance_cities(road_map)
    
    total_cost = compute_total_distance(road_map)
    
    return f" The connections between the cities are as follows: {cities}, the cost between each connection is as follows: {cost}, and the total cost is {total_cost}."



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
        print(road_map)

        result = find_best_cycle(road_map)
        return print_map(result)
    

final = main(r"C:\Users\Diana Jaganjac\pop-one-project-djagan01\city-data.txt")
print(final)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    