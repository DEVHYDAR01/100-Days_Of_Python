from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Famous Arcade Game: The Pong Game")
paddle = Turtle()
screen.listen()
paddle.penup()
screen.tracer(0)

paddle.color("white")
paddle.shape("square")
paddle.setheading(90)
paddle.turtlesize(stretch_len=5)
paddle.goto(x=360, y=0)



def up():
    paddle.fd(20)


def down():
    paddle.bk(20)

    
game_on = True
while game_on:
    screen.update()
    screen.onkey(fun=up, key="Up")
    screen.onkey(fun=down, key="Down")


screen.exitonclick()