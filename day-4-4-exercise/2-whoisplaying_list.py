#!/usr/bin/env python3
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
list_len = len(names)
gen_rand = random.randint(0, list_len)
if gen_rand == 0:
    print(f"{names[0]} is going to buy the meal today!")
elif gen_rand == 1:
    print(f"{names[1]} is going to buy the meal today!")
else:
    print(f"{names[2]} is going to buy the meal today!")
