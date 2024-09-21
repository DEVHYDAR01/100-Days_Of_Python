from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()

        self.color("white")
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.turtlesize(stretch_len=5)
        self.goto(coordinates)

    def up(self):
        self.fd(20)

    def down(self):
        self.bk(20)
