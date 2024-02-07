#!/usr/bin/env python3
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()
lower_name =  lower_name1 + lower_name2

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
add_true = t + r + u + e
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
add_love = l + o + v + e
adding_love_score = str(add_true) + str(add_love)
convert_to_int = int(adding_love_score)
if convert_to_int < 10 or convert_to_int > 90:
  print(f"Your score is {convert_to_int}, you go together like coke and mentos.")
elif convert_to_int >= 40 and convert_to_int <= 50:
  print(f"Your score is {convert_to_int}, you are alright together.")
else:
  print(f"Your score is {convert_to_int}.")
