## Grading Program


# Instructions

You have access to a database of `student_scores` in the format of a dictionary. The **keys** in `student_scores` are the **names** of the students and the **values** are their exam **scores**. 

Write a program that **converts their scores to grades**. By the end of your program, you should have a new dictionary called `student_grades` that should contain student **names** for **keys** and their **grades** for **values**. **The final version** of the `student_grades` dictionary will be checked. 

**DO NOT** modify lines 1-7 to change the existing `student_scores` dictionary. 

**DO NOT** write any print statements.

This is the scoring criteria:

> Scores 91 - 100: Grade = "Outstanding"

> Scores 81 - 90: Grade = "Exceeds Expectations"

> Scores 71 - 80: Grade = "Acceptable"

> Scores 70 or lower: Grade = "Fail"

# Expected Output

```
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
```

# Hint

1. Remember that looping through a Dictionary will only give you the **keys** and not the values. 

2. If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values. 

3. At the **end** of your program, the print statement will show the final `student_scores` dictionary, do not change this.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-9-1-test-your-code](https://repl.it/@appbrewery/day-9-1-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 


# Solution

[https://repl.it/@appbrewery/day-9-1-solution](https://repl.it/@appbrewery/day-9-1-solution)

## Dictionary in List



# Instructions

You are going to write a program that adds to a `travel_log`. You can see a travel_log which is a **List** that contains 2 **Dictionaries**. 

Write a function that will work with the following line of code on line 21 to add the entry for Russia to the `travel_log`. 

```
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
```

> `You've visited Russia 2 times.`

> `You've been to Moscow and Saint Petersburg.`

**DO NOT** modify the `travel_log` directly. You need to create a function that modifies it. 

# Hint

1. Look at the function call above to see what the name of the function should be.

2. The inputs for the function are positional arguments. The order is very important.

3. Feel free to choose your own parameter names.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-9-2-test-your-code](https://repl.it/@appbrewery/day-9-2-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 


# Solution

[https://repl.it/@appbrewery/day-9-2-solution](https://repl.it/@appbrewery/day-9-2-solution)
