#!/usr/bin/env python3

import random

numbers = []

for number in range(1, 101):
    numbers.append(number)
print(numbers)

get_ran_number = random.choice(numbers)
print(get_ran_number)

def compare(user_guessed, get_ran_number):
    if user_guessed < get_ran_number:
        print("Too low")
        print("Guess again")
        return f"you have {attempts} attempts remaining to guess the number"
    elif user_guessed > get_ran_number:
        print("Too High.")
        print("Guess again.")
        return f"you have {attempts} attempts remaining to guess the number"
    elif user_guessed == get_ran_number:
        return f"You got it ! The answer was {get_ran_number}"
    elif attempts == 0 and user_guessed < get_ran_number:
        print("Too low.")
        return 'you have ran out of guesses you lose'
    elif attempts == 0 and user_guessed > get_ran_number:
        print("Too high.")
        return "you have ran out of guesses you lose"

diffculty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if diffculty_level == "easy":
    attempts = 10
    while 0 < attempts:
        print(f"you have {attempts} attempts remaining to guess the number.")
        user_guessed = int(input("make a guess: ").lower())
        compare(user_guessed, get_ran_number)
        attempts = attempts - 1 
elif diffculty_level == "hard":
    attempts = 5
    while 0 < attempts:
        print(f"you have {attempts} attempts remaining to guess the number.")
        user_guessed = int(input("make a guess: ").lower())
        compare(user_guessed, get_ran_number)
        attempts = attempts - 1



