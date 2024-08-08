from turtle import Turtle, Screen

hydar = Turtle()

for i in range(15):
    hydar.forward(10)
    hydar.penup()
    hydar.forward(10)
    hydar.pendown()

my_screen = Screen()
my_screen.exitonclick()