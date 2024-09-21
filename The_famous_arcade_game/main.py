from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Famous Arcade Game: The Pong Game")
screen.tracer(0)
ball = Ball()
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()


screen.exitonclick()