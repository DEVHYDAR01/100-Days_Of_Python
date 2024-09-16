from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
x_coordinates = [(0, 0), (-20, 0), (-40, 0)]
new_snake = []

for turtle in x_coordinates:
    snake = Turtle(shape="square")
    snake.penup()
    snake.goto(turtle)
    snake.color("white")
    new_snake.append(snake)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.5)
    # for snake in new_snake:
    #     snake.fd(20)
    # new_snake[0].right(90)
    for snake in range(len(new_snake) - 1, -1):
        new_x = 


screen.exitonclick()
