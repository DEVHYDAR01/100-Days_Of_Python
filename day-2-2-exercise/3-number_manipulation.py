#!/usr/bin/python
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
years_to_live = int(90)
int_age = int(age)
remaining_years = years_to_live - int_age
days = remaining_years * 365
weeks = remaining_years * 52
months = remaining_years * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
