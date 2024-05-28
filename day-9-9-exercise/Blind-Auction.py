#!/usr/bin/env python3

from os import system
from art import logo

print(logo)
print("Welcome to the secret auction program.")
isTrue = True
#creating a the dictionary for the auction
auction_dict = {}
while isTrue:
    
    get_namekey = input("what is your name?: ")
    get_bidvalue = int(input("what's your bid?: $"))
    auction_dict[get_namekey] = get_bidvalue
    
    any_bidders = input("Are there any bidders? Type 'yes' or 'no': ").lower()
    if any_bidders == "yes":
        system("clear")
    elif any_bidders == "no":
        isTrue = False
    else:
        print("Enter a valid choice!")

bid_tracking = []
for key in auction_dict:
    bid = auction_dict[key]
    bid_tracking.append(bid)

base_case = bid_tracking[0]
for bid in bid_tracking[1:]:
    if bid > base_case:
        max_val = bid

for key in auction_dict:
    if auction_dict[key] == max_val:
        winner = key
print(f"The winner is {winner} with a bid of ${max_val}")