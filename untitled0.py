# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:20:39 2019

@author: Diana Jaganjac
"""

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
    
z = read_cities(r"C:\Users\Diana Jaganjac\pop-one-project-djagan01\city-data.txt")
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


road_map = print_cities(z)
print(road_map[1])