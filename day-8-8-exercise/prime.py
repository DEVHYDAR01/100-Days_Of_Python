#!/usr/bin/env python
def prime(number):
    if number <= 1:
        print("not prime")
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print("not prime")
                break
        else:
            print("prime")

number = int(input("Enter your number:"))

prime(number)