from turtle import Turtle, Screen

tess = Turtle()
screen = Screen()


def forward():
    tess.fd(10)


def backward():
    tess.bk(10)


def clockwise():
    tess.right(10)


def counter_clockwise():
    tess.left(10)


def right_forward():
    tess.right(10)
    tess.forward(10)


def clear_origin():
    screen.resetscreen()


screen.onkey(key="s", fun=backward)
screen.onkey(key="w", fun=forward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_origin)

screen.listen()
screen.exitonclick()