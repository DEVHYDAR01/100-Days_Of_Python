#!/usr/bin/python3
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
length = float(height)
width = int(weight)
bmi = width / length ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
