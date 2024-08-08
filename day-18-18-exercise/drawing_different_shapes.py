from turtle import Turtle, Screen
import random

hydar = Turtle()
colors = ["dark green", "dark slate gray", "maroon", "green yellow", "indigo", "medium violet red"]
number_of_sides = [3, 4, 5, 6, 7, 8, 9, 10]
for i in number_of_sides:
    if i == 3:
        for sides in range(i):
            hydar.forward(100)
            hydar.left(120)
        hydar.forward(100)
    else:
        for sides in range(i):
            hydar.color(random.choice(colors))
            corner_angle = 360 / i
            hydar.left(round(corner_angle))
            hydar.fd(100)
my_screen = Screen()
my_screen.exitonclick()