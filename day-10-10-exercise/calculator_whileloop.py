#!/usr/bin/env python3

from art import logo
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Creating a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))

    for key in operations:
        if key == operation_symbol:
            function = operations[key]
            answer = function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    ops_continue = True
    while ops_continue:
        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, type 'n' to exit: ").lower()
        if continue_calculating == "n":
            ops_continue = False
            calculator()
        elif continue_calculating == "y":
            operation_symbol = input("Pick an operation: ")
            next_number = int(input("What's the next number?: "))
            for key in operations:
                if key == operation_symbol:
                    function = operations[key]
                    continue_answer = function(answer, next_number)
                    answer = continue_answer
            print(f"{answer} {operation_symbol} {next_number} = {continue_answer}")
        else:
            print("Invalid input. Please type 'y' to continue or 'n' to exit.")

calculator()