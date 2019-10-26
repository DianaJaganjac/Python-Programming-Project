import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)
    

def test_compute_total_distance():   
    road_map4 = [("California", "Sacramento", 38.555605, -121.468926),\
		("Colorado",	"Denver",	39.7391667,	-104.984167),\
		("Connecticut",	"Hartford",	41.767,	-72.677)]
		                           
    assert compute_total_distance(road_map4)==\
           pytest.approx(16.484 + 32.307 + 48.791, 0.01)