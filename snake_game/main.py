from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect food collision
    if snake.new_snake[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_score()

    # Detect wall collision
    if (snake.new_snake[0].xcor() > 280 or snake.new_snake[0].xcor() < -280 or snake.new_snake[0].ycor() > 290
            or snake.new_snake[0].ycor() < -290):
        scoreboard.score_reset()
        snake.reset()

    # Detect tail collision
    for seg in snake.new_snake[1:]:
        if snake.new_snake[0].distance(seg) < 10:
            scoreboard.score_reset()
            snake.reset()

screen.exitonclick()
