#!/usr/bin/env python3
#Write your code below this line 👇
def prime_checker(number):
    if number > 1 and number % number == 1 and number / 1 == number :
        print("prime")
    else:
        print("not prime")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
