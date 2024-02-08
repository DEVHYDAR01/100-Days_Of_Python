#!/usr/bin/env python3
import random
# Don't change the code below
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# Don't change the code above
# Write your code below this line
#Hint: Remember to import the random module first. 🎲
seed_toss = random.randint(0, 1)
if seed_toss == 1:
    print("Heads")
else:
    print("Tails")
