# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:20:39 2019

@author: Diana Jaganjac
"""
import random 

d = [1,2,3,4,5,7,3,4]

N = (len(d)-1)

number = int(N * random.random())
print(number)

 current_cycle_1 = compute_total_distance(road_map)
        if current_cycle_1 < best_cycle_1:
            best_cycle_1 = current_cycle_1
    
        cycle2 = shift_cities(road_map)
        current_cycle_2 = compute_total_distance(road_map)
        if current_cycle_2 < best_cycle_2:
            best_cycle_2 = current_cycle_2
    
    if best_cycle_1 < best_cycle_2:
        return cycle1, current_cycle_1
    else:
        return cycle2, current_cycle_2

