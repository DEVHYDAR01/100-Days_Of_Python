#!/usr/bin/env python3
total = 0
count = 0
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
  total = total + student_heights[n]
for i in student_heights:
    count = count + 1
average_height = round(total / count)
print(average_height)