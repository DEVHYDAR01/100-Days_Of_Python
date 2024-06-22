#!/usr/bin/env python3
from art import logo, vs
from game_data import data
import random

def gen_random_dict(data):
    '''This function will generate and return a random dictionary from a list containing dictionaries'''
    dict = random.choice(data)
    return dict

def dict_update(compare):
    update_dict = gen_random_dict(data)
    for key in update_dict:
        compare[key] = update_dict[key]
    print(update_dict)
    return compare  

compare_a = {}
compare_b = {}
# print(logo)
# print(vs)
update_a = dict_update(compare_a)
update_b = dict_update(compare_b)


print(f"The length of data if {len(data)}")