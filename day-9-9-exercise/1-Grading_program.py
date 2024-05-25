#!/usr/bin/env python3
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    names = key
    scores = student_scores[key]
    if scores == 91 or scores > 91:
        student_grades[names] = "Oustanding"
    elif scores == 81 or scores > 81:
        student_grades[names] = "Exceeds Expectations"
    elif scores == 71 or scores > 71:
        student_grades[names] = "Acceptable"
    elif scores == 70 or scores < 70:
        student_grades[names] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)