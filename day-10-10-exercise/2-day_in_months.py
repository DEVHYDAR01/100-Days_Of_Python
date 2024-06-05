#!/usr/bin/env python3
def is_leap(year):
  """This will return true if leap year and false if not"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  

# # # TODO: Add more code here 👇
def days_in_month(year, month):
  """This will accept two parameters check and work out
  the days in month if not leap year and return 29 days if leap and month is 2
  """
  is_leap_checking = is_leap(year)
  print(is_leap_checking)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap_checking == False:
    for days in range(len(month_days)):
      if days == month - 1:
        return month_days[days]
  if is_leap_checking == True and month == 2:
    return 29
  
# #🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)
