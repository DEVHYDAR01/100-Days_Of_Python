from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Famous Arcade Game: The Pong Game")
screen.tracer(0)
ball = Ball()
scoreboard = ScoreBoard()
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")


game_on = True
speed = 0
while game_on:
    time.sleep(ball.speed_move)
    screen.update()
    ball.move()
    # Detect collision with the top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_reset_pos()
        scoreboard.l_paddle_score()

    if ball.xcor() < -380:
        ball.ball_reset_pos()
        scoreboard.r_paddle_score()


screen.exitonclick()