from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)
bob = Turtle()
bob.hideturtle()

color_list = [(200, 10, 35), (247, 236, 37), (240, 244, 251), (239, 231, 3), (36, 216, 77),
              (223, 159, 61), (39, 79, 185), (28, 39, 159), (210, 73, 16), (17, 151, 18), (239, 39, 152), (65, 9, 27),
              (188, 14, 9), (216, 25, 127), (218, 140, 198), (223, 161, 7), (59, 12, 7), (67, 202, 227), (10, 96, 60),
              (84, 80, 212), (17, 19, 52), (237, 157, 218), (106, 232, 195), (99, 205, 136), (212, 84, 58),
              (8, 222, 235), (236, 171, 161)]


def print_circle():
    for r in range(10):
        get_rand_color_tuple = random.choice(color_list)
        bob.dot(20, get_rand_color_tuple)
        bob.penup()
        bob.fd(50)


increment_y = -200
for i in range(10):
    bob.teleport(-200, increment_y)
    print_circle()
    increment_y = increment_y + 50

my_screen = Screen()
my_screen.exitonclick()
