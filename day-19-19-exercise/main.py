from turtle import Turtle, Screen

tess = Turtle()
screen = Screen()
screen.listen()


def forward():
    tess.fd(10)


screen.onkey(key="w", fun=forward)

screen.exitonclick()