from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
my_snake = Snake()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(1)


    my_snake.move()
    print(my_snake.new_snake)

screen.exitonclick()
