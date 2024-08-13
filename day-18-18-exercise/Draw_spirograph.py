import turtle as t
from turtle import Screen
import random

nana = t.Turtle()
t.colormode(255)


def ran_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        nana.speed("fastest")
        nana.circle(100)
        nana.color(ran_colors())
        nana.right(size_of_gap)


spirograph(5)

my_screen = Screen()
my_screen.exitonclick()