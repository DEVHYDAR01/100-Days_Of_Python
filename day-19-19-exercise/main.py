from turtle import Turtle, Screen
import random

screen = Screen()
is_on = False
choose_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter your color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen.setup(width=500, height=400)
y_axis = [-70, -40, -10, 20, 50, 80]
turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_axis[i])
    turtles.append(new_turtle)

if choose_bet:
    is_on = True

while is_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == choose_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
        distance_turtle = random.randint(0, 10)
        turtle.forward(distance_turtle)


screen.exitonclick()