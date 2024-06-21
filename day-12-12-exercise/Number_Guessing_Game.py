#!/usr/bin/env python3

import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
numbers = []
for number in range(1, 101):
    numbers.append(number)
get_ran_number = random.choice(numbers)

def compare_high_and_low(user_guessed, get_ran_number):
    if user_guessed < get_ran_number:
        print("Too low")
        print("Guess again")
        return f"you have {attempts} attempts remaining to guess the number"
    elif user_guessed > get_ran_number:
        print("Too High.")
        print("Guess again.")
        return f"you have {attempts} attempts remaining to guess the number"


diffculty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if diffculty_level == "easy":
    attempts = 10
    while 0 < attempts:
        print(f"you have {attempts} attempts remaining to guess the number.")
        user_guessed = int(input("make a guess: ").lower())
        if user_guessed == get_ran_number:
            print(f"You got it ! The answer was {get_ran_number}")
            break
        elif attempts == 1 and user_guessed < get_ran_number:
            print("Too low.")
            print('you have ran out of guesses you lose')
            break
        elif attempts == 1 and user_guessed > get_ran_number:
            print("Too high.")
            print("you have ran out of guesses you lose")
            break
        compare_high_and_low(user_guessed, get_ran_number)
        attempts = attempts - 1 
elif diffculty_level == "hard":
    attempts = 5
    while 0 < attempts:
        print(f"you have {attempts} attempts remaining to guess the number.")
        user_guessed = int(input("make a guess: ").lower())
        if user_guessed == get_ran_number:
            print(f"You got it ! The answer was {get_ran_number}")
            break
        elif attempts == 1 and user_guessed < get_ran_number:
            print("Too low.")
            print('you have ran out of guesses you lose')
            break
        elif attempts == 1 and user_guessed > get_ran_number:
            print("Too high.")
            print("you have ran out of guesses you lose")
            break
        compare_high_and_low(user_guessed, get_ran_number)
        attempts = attempts - 1



