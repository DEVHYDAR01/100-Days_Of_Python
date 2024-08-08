from turtle import Turtle, Screen

hydar = Turtle()

hydar.shape("turtle")
hydar.color("red")
for i in range(4):
    hydar.forward(100)
    hydar.left(90)
my_screen = Screen()
my_screen.exitonclick()

