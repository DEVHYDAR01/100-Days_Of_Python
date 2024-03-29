#!/usr/bin/env python3
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#randomize letters
list_letters = []
list_numbers = []
list_symbols = []
ran_list_result = []
for letter in letters:
    ran_letters = random.choice(letters)
    list_letters.append(ran_letters)
#print(list_letters)
for i in range(0, nr_letters):
    ran_list_result.append(list_letters[i])

#randomize numbers
for number in numbers:
    ran_numbers = random.choice(numbers)
    list_numbers.append(ran_numbers)
#print(list_numbers)
for j in range(0, nr_numbers):
    ran_list_result.append(list_numbers[j])

#randomize symbols
for symbol in symbols:
    ran_symbols = random.choice(symbols)
    list_symbols.append(ran_symbols)
for k in range(0, nr_symbols):
    ran_list_result.append(list_symbols[k])
password_gen = ''.join(ran_list_result)
print(f"Here is your password: {password_gen}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P