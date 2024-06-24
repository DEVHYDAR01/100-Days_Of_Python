#!/usr/bin/env python3
from art import logo, vs
from game_data import data
import random

def gen_random_dict(data):
    '''This function will generate and return a random dictionary from a list containing dictionaries'''
    dict = random.choice(data)
    return dict

def dict_update(compare):
    '''This function will generate a random dictionary take in an empty one populate it with the values of the random one and return it  '''
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

def get_values(compare, which):
    """This funtion will take in a dictionary and string of what i am comparing,extract the values of the corresponding keys and returns them."""
    get_name = compare["name"]
    get_description = compare["description"]
    get_country = compare["country"]
    return f"{which}: {get_name}, {get_description}, from {get_country}"

get_values_a = get_values(compare_a, "Compare A")
get_values_b = get_values(compare_b, "Compare B")
print(get_values_a)
print(get_values_b)

def extract_follower_count(compare):
    """This function takes in a dictionary and returns the follower count"""
    get_follower_count = compare["follower_count"]
    return get_follower_count

get_follower_count_a = extract_follower_count(compare_a)
get_follower_count_b = extract_follower_count(compare_b)
print(get_follower_count_a)
print(get_follower_count_b)


isTrue = True
while isTrue:
    score_count = 0
    more_followers = input("Who has more followers? Type 'A' or 'B': ").lower()
    if more_followers == 'a':
        if get_follower_count_a > get_follower_count_b:
            score_count = score_count + 1
            update_a = update_b
            update_b = gen_random_dict(data)
            get_values_a = get_values(update_a, "Compare A")
            get_values_b = get_values(update_b, "Compare B")
            print(get_values_a)
            print(get_values_b)
            get_follower_count_a = extract_follower_count(update_a)
            get_follower_count_b = extract_follower_count(update_b)
            print(get_follower_count_a)
            print(get_follower_count_b)
            print(update_a)
            print(update_b)
    else:
        print(F"sorry, that's wrong. Final score: {score_count}")
        isTrue = False
    # elif more_followers == 'b':
    #     if get_follower_count_b > get_follower_count_a:
    #         score_count = score_count + 1
print(score_count)

# print(f"The length of data if {len(data)}")