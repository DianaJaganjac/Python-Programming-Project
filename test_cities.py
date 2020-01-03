import pytest
from pytest import *
import cities
from cities import *
import copy

def test_compute_total_distance():
    total = cities.compute_total_distance(road_map)
    assert total == approx(1039.64)
    
    total = cities.compute_total_distance(road_map)
    assert type(total) == float

    new_road_map = [ ('Juneau', 58.3, -134.42),\
                     ('Phoenix', 33.45, -112.07), ('Little Rock', 34.74, -92.33),\
                     ('Sacramento', 38.56, -121.47), ('Denver', 39.74, -104.98),\
                     ('Hartford', 41.77, -72.68), ('Dover', 39.16, -75.53),\
                     ('Tallahassee', 30.45, -84.27), ('Atlanta', 33.76, -84.39),\
                     ('Honolulu', 21.31, -157.83), ('Boise', 43.61, -116.24),\
                     ('Springfield', 39.78, -89.65), ('Indianapolis', 39.79, -86.15),\
                     ('Des Moines', 41.59, -93.62), ('Topeka', 39.04, -95.69),\
                     ('Frankfort', 38.2, -84.86), ('Baton Rouge', 30.46, -91.14),\
                     ('Augusta', 44.32, -69.77), ('Annapolis', 38.97, -76.5),\
                     ('Boston', 42.24, -71.03), ('Lansing', 42.73, -84.55),\
                     ('Saint Paul', 44.95, -93.09), ('Jackson', 32.32, -90.21), \
                     ('Jefferson City', 38.57, -92.19), ('Helana', 46.6, -112.03),\
                     ('Lincoln', 40.81, -96.68), ('Carson City', 39.16, -119.75),\
                     ('Concord', 43.22, -71.55), ('Trenton', 40.22, -74.76),\
                     ('Santa Fe', 35.67, -105.96), ('Albany', 42.66, -73.78),\
                     ('Raleigh', 35.77, -78.64), ('Bismarck', 48.81, -100.78),\
                     ('Columbus', 39.96, -83.0), ('Oklahoma City', 35.48, -97.53),\
                     ('Salem', 44.93, -123.03), ('Harrisburg', 40.27, -76.88), \
                     ('Providence', 41.82, -71.42), ('Columbia', 34.0, -81.03),\
                     ('Pierre', 44.37, -100.34), ('Nashville', 36.16, -86.78),\
                     ('Austin', 30.27, -97.75), ('Salt Lake City', 40.75, -111.89),\
                     ('Montpelier', 44.27, -72.57), ('Richmond', 37.54, -77.46),\
                     ('Olympia', 47.04, -122.89), ('Charleston', 38.35, -81.63),\
                     ('Madison', 43.07, -89.38), ('Cheyenne', 41.15, -104.8)]
                     
    total = cities.compute_total_distance(new_road_map)                 
    assert total == approx(984.96)

    new_road_map = [ ('Juneau', 58.3, -134.42),\
                     ('Phoenix', 33.45, -112.07), ('Little Rock', 34.74, -92.33),\
                     ('Sacramento', 38.56, -121.47), ('Denver', 39.74, -104.98),\
                     ('Hartford', 41.77, -72.68), ('Dover', 39.16, -75.53),\
                     ('Tallahassee', 30.45, -84.27), ('Atlanta', 33.76, -84.39),\
                     ('Honolulu', 21.31, -157.83), ('Boise', 43.61, -116.24),\
                     ('Springfield', 39.78, -89.65), ('Indianapolis', 39.79, -86.15),\
                     ('Des Moines', 41.59, -93.62), ('Topeka', 39.04, -95.69),\
                     ('Frankfort', 38.2, -84.86), ('Baton Rouge', 30.46, -91.14),\
                     ('Augusta', 44.32, -69.77), ('Annapolis', 38.97, -76.5),\
                     ('Boston', 42.24, -71.03), ('Lansing', 42.73, -84.55),\
                     ('Saint Paul', 44.95, -93.09), ('Jackson', 32.32, -90.21), \
                     ('Jefferson City', 38.57, -92.19), ('Helana', 46.6, -112.03),\
                     ('Lincoln', 40.81, -96.68), ('Carson City', 39.16, -119.75),\
                     ('Concord', 43.22, -71.55), ('Trenton', 40.22, -74.76),\
                     ('Santa Fe', 35.67, -105.96), ('Albany', 42.66, -73.78),\
                     ('Raleigh', 35.77, -78.64), ('Bismarck', 48.81, -100.78),\
                     ('Columbus', 39.96, -83.0), ('Oklahoma City', 35.48, -97.53),\
                     ('Salem', 44.93, -123.03), ('Harrisburg', 40.27, -76.88), \
                     ('Pierre', 44.37, -100.34), ('Nashville', 36.16, -86.78),\
                     ('Austin', 30.27, -97.75), ('Salt Lake City', 40.75, -111.89),\
                     ('Montpelier', 44.27, -72.57), ('Richmond', 37.54, -77.46),\
                     ('Olympia', 47.04, -122.89), ('Charleston', 38.35, -81.63),\
                     ('Madison', 43.07, -89.38), ('Cheyenne', 41.15, -104.8)]

    total = cities.compute_total_distance(new_road_map)
    assert total == approx(968.79)
    
    new_road_map = [ ('Juneau', 58.3, -134.42),\
                     ('Phoenix', 33.45, -112.07), ('Little Rock', 34.74, -92.33),\
                     ('Sacramento', 38.56, -121.47), ('Denver', 39.74, -104.98),\
                     ('Hartford', 41.77, -72.68), ('Dover', 39.16, -75.53),\
                     ('Tallahassee', 30.45, -84.27), ('Atlanta', 33.76, -84.39),\
                     ('Jefferson City', 38.57, -92.19), ('Helana', 46.6, -112.03),\
                     ('Lincoln', 40.81, -96.68), ('Carson City', 39.16, -119.75),\
                     ('Concord', 43.22, -71.55), ('Trenton', 40.22, -74.76),\
                     ('Santa Fe', 35.67, -105.96), ('Albany', 42.66, -73.78),\
                     ('Raleigh', 35.77, -78.64), ('Bismarck', 48.81, -100.78),\
                     ('Columbus', 39.96, -83.0), ('Oklahoma City', 35.48, -97.53),\
                     ('Salem', 44.93, -123.03), ('Harrisburg', 40.27, -76.88), \
                     ('Pierre', 44.37, -100.34), ('Nashville', 36.16, -86.78),\
                     ('Austin', 30.27, -97.75), ('Salt Lake City', 40.75, -111.89),\
                     ('Montpelier', 44.27, -72.57), ('Richmond', 37.54, -77.46),\
                     ('Olympia', 47.04, -122.89), ('Charleston', 38.35, -81.63),\
                     ('Madison', 43.07, -89.38), ('Cheyenne', 41.15, -104.8)]

    total = cities.compute_total_distance(new_road_map)
    assert total == approx(711.81)
    
    new_road_map = [ ('Juneau', 58.3, -134.42),\
                     ('Phoenix', 33.45, -112.07), ('Little Rock', 34.74, -92.33),\
                     ('Sacramento', 38.56, -121.47), ('Denver', 39.74, -104.98),\
                     ('Columbus', 39.96, -83.0), ('Oklahoma City', 35.48, -97.53),\
                     ('Salem', 44.93, -123.03), ('Harrisburg', 40.27, -76.88), \
                     ('Pierre', 44.37, -100.34), ('Nashville', 36.16, -86.78),\
                     ('Austin', 30.27, -97.75), ('Salt Lake City', 40.75, -111.89),\
                     ('Montpelier', 44.27, -72.57), ('Richmond', 37.54, -77.46),\
                     ('Olympia', 47.04, -122.89), ('Charleston', 38.35, -81.63),\
                     ('Madison', 43.07, -89.38), ('Cheyenne', 41.15, -104.8)]

    total = cities.compute_total_distance(new_road_map)
    assert total == approx(440.6)

    new_road_map = [ ('X', 43.3, -22.34), ('Y', 35.78, -68.99), ('Z', 90.00, -180.00)]
    total = cities.compute_total_distance(new_road_map)
    assert total == approx(170.8)

    new_road_map = [ ('X', 90.0, 180.0),('Y', -90.0, -180.0), ('Z', 0.00, 0.00)]
    total = cities.compute_total_distance(new_road_map)
    assert total == approx(603.74)

    new_road_map = [ ('X', 50.0, 150.0),('Y', -50.0, -150.0), ('Z', 100.00, -100.00)]    
    total = cities.compute_total_distance(new_road_map)
    assert total == approx(474.34)
    
    new_road_map = [ ('X', 700000.0, 0.0),('Y', 3699900.0, -367880.0), ('Z', -10000.00, -100.00)]
    total = cities.compute_total_distance(new_road_map)
    assert total == approx(6750457.85)

def test_swap_cities():

    total = cities.swap_cities(road_map, 0, 12)

    assert total == ([('Springfield', 39.78, -89.65),('Juneau', 58.3, -134.42),\
                         ('Phoenix', 33.45, -112.07), ('Little Rock', 34.74, -92.33),\
                         ('Sacramento', 38.56, -121.47), ('Denver', 39.74, -104.98),\
                         ('Hartford', 41.77, -72.68), ('Dover', 39.16, -75.53),\
                         ('Tallahassee', 30.45, -84.27), ('Atlanta', 33.76, -84.39),\
                         ('Honolulu', 21.31, -157.83), ('Boise', 43.61, -116.24),\
                         ('Montgomery', 32.36, -86.28), ('Indianapolis', 39.79, -86.15),\
                         ('Des Moines', 41.59, -93.62), ('Topeka', 39.04, -95.69),\
                         ('Frankfort', 38.2, -84.86), ('Baton Rouge', 30.46, -91.14),\
                         ('Augusta', 44.32, -69.77), ('Annapolis', 38.97, -76.5),\
                         ('Boston', 42.24, -71.03), ('Lansing', 42.73, -84.55),\
                         ('Saint Paul', 44.95, -93.09), ('Jackson', 32.32, -90.21), \
                         ('Jefferson City', 38.57, -92.19), ('Helana', 46.6, -112.03),\
                         ('Lincoln', 40.81, -96.68), ('Carson City', 39.16, -119.75),\
                         ('Concord', 43.22, -71.55), ('Trenton', 40.22, -74.76),\
                         ('Santa Fe', 35.67, -105.96), ('Albany', 42.66, -73.78),\
                         ('Raleigh', 35.77, -78.64), ('Bismarck', 48.81, -100.78),\
                         ('Columbus', 39.96, -83.0), ('Oklahoma City', 35.48, -97.53),\
                         ('Salem', 44.93, -123.03), ('Harrisburg', 40.27, -76.88), \
                         ('Providence', 41.82, -71.42), ('Columbia', 34.0, -81.03),\
                         ('Pierre', 44.37, -100.34), ('Nashville', 36.16, -86.78),\
                         ('Austin', 30.27, -97.75), ('Salt Lake City', 40.75, -111.89),\
                         ('Montpelier', 44.27, -72.57), ('Richmond', 37.54, -77.46),\
                         ('Olympia', 47.04, -122.89), ('Charleston', 38.35, -81.63),\
                         ('Madison', 43.07, -89.38), ('Cheyenne', 41.15, -104.8)], 1042.48)


    new_road_map = [('Springfield', 39.78, -89.65),('Juneau', 58.3, -134.42),\
                         ('Phoenix', 33.45, -112.07), ('Little Rock', 34.74, -92.33),\
                         ('Sacramento', 38.56, -121.47), ('Denver', 39.74, -104.98),\
                         ('Hartford', 41.77, -72.68), ('Dover', 39.16, -75.53),\
                         ('Tallahassee', 30.45, -84.27), ('Atlanta', 33.76, -84.39),\
                         ('Honolulu', 21.31, -157.83), ('Boise', 43.61, -116.24),\
                         ('Montgomery', 32.36, -86.28), ('Indianapolis', 39.79, -86.15)]

    total = cities.swap_cities(new_road_map, 3, 6)
    assert total == ([('Springfield', 39.78, -89.65),('Juneau', 58.3, -134.42),\
                         ('Phoenix', 33.45, -112.07), ('Hartford', 41.77, -72.68),\
                         ('Sacramento', 38.56, -121.47), ('Denver', 39.74, -104.98),\
                         ('Little Rock', 34.74, -92.33), ('Dover', 39.16, -75.53),\
                         ('Tallahassee', 30.45, -84.27), ('Atlanta', 33.76, -84.39),\
                         ('Honolulu', 21.31, -157.83), ('Boise', 43.61, -116.24),\
                         ('Montgomery', 32.36, -86.28), ('Indianapolis', 39.79, -86.15)], 395.3)


    new_road_map = [('Springfield', 39.78, -89.65),('Juneau', 58.3, -134.42),\
                         ('Phoenix', 33.45, -112.07), ('Little Rock', 34.74, -92.33),\
                         ('Sacramento', 38.56, -121.47), ('Denver', 39.74, -104.98),\
                         ('Hartford', 41.77, -72.68), ('Dover', 39.16, -75.53)]
                         
    total = cities.swap_cities(new_road_map, 2, 5)
                         
    assert total == ([('Springfield', 39.78, -89.65),('Juneau', 58.3, -134.42),\
                         ('Denver', 39.74, -104.98), ('Little Rock', 34.74, -92.33),\
                         ('Sacramento', 38.56, -121.47), ('Phoenix', 33.45, -112.07),\
                         ('Hartford', 41.77, -72.68), ('Dover', 39.16, -75.53)], 181.07)

    

    new_road_map = [('Phoenix', 33.45, -112.07), ('Little Rock', 77.0, -7903224),\
                         ('Sacramento', 38.56, -121.47), ('Denver', 39.74, -104.98),\
                         ('Hartford', 41.77, -98.68), ('Dover', 88.16, -75.53)]
    
    total = cities.swap_cities(new_road_map, 2, 4)
    assert total == ([('Phoenix', 33.45, -112.07), ('Little Rock', 77.0, -7903224),\
                      ('Hartford', 41.77, -98.68), ('Denver', 39.74, -104.98),\
                      ('Sacramento', 38.56, -121.47), ('Dover', 88.16, -75.53)], 15806328.01)

    new_road_map = [('Saint Paul', 44.95, -93.09), ('Jackson', 32.32, -90.21), \
                         ('Jefferson City', 38.57, -92.19), ('Helana', 46.6, -112.03),\
                         ('Lincoln', 40.81, -96.68), ('Carson City', 39.16, -119.75),\
                         ('Concord', 43.22, -71.55), ('Trenton', 40.22, -74.76),\
                         ('Santa Fe', 35.67, -105.96), ('Albany', 42.66, -73.78)]


    total = cities.swap_cities(new_road_map, 4, 4)
    assert total == ([('Saint Paul', 44.95, -93.09), ('Jackson', 32.32, -90.21), \
                         ('Jefferson City', 38.57, -92.19), ('Helana', 46.6, -112.03),\
                         ('Lincoln', 40.81, -96.68), ('Carson City', 39.16, -119.75),\
                         ('Concord', 43.22, -71.55), ('Trenton', 40.22, -74.76),\
                         ('Santa Fe', 35.67, -105.96), ('Albany', 42.66, -73.78)], 197.67)
                      



    

def test_shift_cities():

    total = cities.shift_cities(road_map)
    assert total == ([('Cheyenne', 41.15, -104.8), ('Montgomery', 32.36, -86.28), \
                      ('Juneau', 58.3, -134.42), ('Phoenix', 33.45, -112.07), \
                      ('Little Rock', 34.74, -92.33), ('Sacramento', 38.56, -121.47), \
                      ('Denver', 39.74, -104.98), ('Hartford', 41.77, -72.68),\
                      ('Dover', 39.16, -75.53), ('Tallahassee', 30.45, -84.27), \
                      ('Atlanta', 33.76, -84.39), ('Honolulu', 21.31, -157.83), \
                      ('Boise', 43.61, -116.24), ('Springfield', 39.78, -89.65), \
                      ('Indianapolis', 39.79, -86.15), ('Des Moines', 41.59, -93.62),\
                      ('Topeka', 39.04, -95.69), ('Frankfort', 38.2, -84.86), \
                      ('Baton Rouge', 30.46, -91.14), ('Augusta', 44.32, -69.77),\
                      ('Annapolis', 38.97, -76.5), ('Boston', 42.24, -71.03),\
                      ('Lansing', 42.73, -84.55), ('Saint Paul', 44.95, -93.09), \
                      ('Jackson', 32.32, -90.21), ('Jefferson City', 38.57, -92.19), \
                      ('Helana', 46.6, -112.03), ('Lincoln', 40.81, -96.68),\
                      ('Carson City', 39.16, -119.75), ('Concord', 43.22, -71.55),\
                      ('Trenton', 40.22, -74.76), ('Santa Fe', 35.67, -105.96),\
                      ('Albany', 42.66, -73.78), ('Raleigh', 35.77, -78.64), \
                      ('Bismarck', 48.81, -100.78), ('Columbus', 39.96, -83.0), \
                      ('Oklahoma City', 35.48, -97.53), ('Salem', 44.93, -123.03), \
                      ('Harrisburg', 40.27, -76.88), ('Providence', 41.82, -71.42),\
                      ('Columbia', 34.0, -81.03), ('Pierre', 44.37, -100.34),\
                      ('Nashville', 36.16, -86.78), ('Austin', 30.27, -97.75), \
                      ('Salt Lake City', 40.75, -111.89), ('Montpelier', 44.27, -72.57), \
                      ('Richmond', 37.54, -77.46), ('Olympia', 47.04, -122.89),\
                      ('Charleston', 38.35, -81.63), ('Madison', 43.07, -89.38)], 1044.6)

    new_road_map = [('Cheyenne', 41.15, -104.8), ('Montgomery', 32.36, -86.28), \
                      ('Juneau', 58.3, -134.42), ('Phoenix', 33.45, -112.07), \
                      ('Little Rock', 34.74, -92.33), ('Sacramento', 38.56, -121.47), \
                      ('Denver', 39.74, -104.98), ('Hartford', 41.77, -72.68),\
                      ('Dover', 39.16, -75.53), ('Tallahassee', 30.45, -84.27)]
    
    total = cities.shift_cities(new_road_map)
    assert total == ([('Tallahassee', 30.45, -84.27), ('Cheyenne', 41.15, -104.8), \
                      ('Montgomery', 32.36, -86.28), ('Juneau', 58.3, -134.42),\
                      ('Phoenix', 33.45, -112.07), ('Little Rock', 34.74, -92.33),\
                      ('Sacramento', 38.56, -121.47), ('Denver', 39.74, -104.98),\
                      ('Hartford', 41.77, -72.68), ('Dover', 39.16, -75.53)], 233.69)

    new_road_map = [('Carson City', 39.16, -119.75), ('Concord', 43.22, -71.55),\
                      ('Trenton', 40.22, -74.76), ('Santa Fe', 35.67, -105.96),\
                      ('Albany', 42.66, -73.78), ('Raleigh', 35.77, -78.64), \
                      ('Bismarck', 48.81, -100.78), ('Columbus', 39.96, -83.0)]
    
    total = cities.shift_cities(new_road_map)
    
    assert total == ([('Columbus', 39.96, -83.0), ('Carson City', 39.16, -119.75), \
                      ('Concord', 43.22, -71.55), ('Trenton', 40.22, -74.76),\
                      ('Santa Fe', 35.67, -105.96), ('Albany', 42.66, -73.78),\
                      ('Raleigh', 35.77, -78.64), ('Bismarck', 48.81, -100.78)], 188.11)
    
    new_road_map = [('Nashville', 36.16, -86.78), ('Austin', 30.27, -97.75), \
                      ('Salt Lake City', 40.75, -111.89), ('Montpelier', 44.27, -72.57)]
    
    total = cities.shift_cities(new_road_map)
    assert total == ([('Montpelier', 44.27, -72.57), ('Nashville', 36.16, -86.78),\
                      ('Austin', 30.27, -97.75), ('Salt Lake City', 40.75, -111.89)], 46.41)

    new_road_map = [('Carson City', 39.16, -119.75), ('Carson City', 39.16, -119.75),
                    ('Concord', 43.22, -71.55),('Trenton', 40.22, -74.76), \
                    ('Santa Fe', 35.67, -105.96), ('Santa Fe', 35.67, -105.96)]
    
    total = cities.shift_cities(new_road_map)
    assert total == ([('Santa Fe', 35.67, -105.96), ('Carson City', 39.16, -119.75), ('Carson City', 39.16, -119.75),\
                      ('Concord', 43.22, -71.55), ('Trenton', 40.22, -74.76), ('Santa Fe', 35.67, -105.96)], 98.52)
