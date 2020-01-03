import pytest
from cities import *
#
#def read_cities(file_name):
#    """
#    Read in the cities from the given `file_name`, and return 
#    them as a list of four-tuples: 
#      [(state, city, latitude, longitude), ...] 
#    Use this as your initial `road_map`, that is, the cycle 
#      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
#    """
#    f = open(file_name)
#    lines = f.readlines()
#    result = []
#    for line in lines:
#        line = line.strip("\n")
#        ele = line.split("\t")
#        joinele = (ele[0]), (ele[1]), float(ele[2]), float(ele[3])
#        result.append(joinele)
#    return (result)
#    f.close
#    
#z = read_cities(r"C:\Users\Diana Jaganjac\pop-one-project-djagan01\city-data.txt")
##print(z)
#  
#def print_cities(road_map):
#    """
#    Prints a list of cities, along with their locations. 
#    Print only one or two digits after the decimal point.
#    """
#    result = []
#    for ele in road_map:
#        rm = ((ele[1]), (round(ele[2],2)), (round(ele[3],2)))
#        result.append(rm)        
#    return result
#
#
#road_map = print_cities(z)
#print(road_map)

def test_compute_total_distance():
    total = cities.compute_total_distance(road_map)
    assert total == 1039.64
    

    

#def test_compute_total_distance():   
#    road_map4 = [("California", "Sacramento", 38.555605, -121.468926),\
#		("Colorado",	"Denver",	39.7391667,	-104.984167),\
#		("Connecticut",	"Hartford",	41.767,	-72.677)]
#		                           
#    assert compute_total_distance(road_map4)==\
#           pytest.approx(16.484 + 32.307 + 48.791, 0.01)
#
#def test_swap_cities():
#    road_map2 = [("California", "Sacramento", 38.555605, -121.468926),\
#		("Colorado", "Denver", 39.7391667, -104.984167),\
#		("Connecticut",	"Hartford", 41.767, -72.677)]
#
#    assert swap_cities(road_map2, 0, 2)==[("Connecticut", "Hartford", 41.767, -72.677),("Colorado", "Denver", 39.7391667, -104.984167),("California", "Sacramento", 38.555605, -121.468926)]
#
#def test_shift_cities():
#    
#    road_map3 = [("California",	"Sacramento", 38.555605, -121.468926),("Delaware", "Dover", 39.161921, -75.526755),("Florida", "Tallahassee", 30.4518, -84.27277)]
#
#    assert shift_cities(road_map3)==[("Florida","Tallahassee", 30.4518, -84.27277),("California", "Sacramento", 38.555605, -121.468926),("Delaware", "Dover", 39.161921, -75.526755)]
