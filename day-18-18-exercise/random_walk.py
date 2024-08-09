from turtle import Turtle, Screen
import random

nana = Turtle()
colors = ["dark green", "dark slate gray", "maroon", "green yellow", "indigo", "medium violet red"]


def forward(steps):
    nana.color(random.choice(colors))
    nana.pensize(5)
    nana.speed("fastest")
    return nana.forward(steps)


def backward(steps):
    nana.color(random.choice(colors))
    nana.pensize(5)
    nana.speed("fastest")
    return nana.backward(steps)


def right(steps):
    nana.color(random.choice(colors))
    nana.pensize(5)
    nana.speed("fastest")
    return nana.right(steps)


def left(steps):
    nana.color(random.choice(colors))
    nana.pensize(5)
    nana.speed("fastest")
    return nana.left(steps)


motion = [forward, backward, right, left]

for i in range(2000):
    random_walk = random.choice(motion)
    print(random_walk)
    if random_walk == forward:
        random_walk(10)
    elif random_walk == backward:
        random_walk(10)
    else:
        random_walk(90)


my_screen = Screen()
my_screen.exitonclick()
