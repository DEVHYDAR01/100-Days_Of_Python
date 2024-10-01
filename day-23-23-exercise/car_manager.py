from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1.9, stretch_wid=0.95)
        self.penup()
        self.setheading(180)
        self.goto(300, 0)

    # def y_pos(self):
    #     pos_y = random.randint(300, -300)
    #     self.goto(300, pos_y)

    def car_movement(self):
        self.fd(STARTING_MOVE_DISTANCE)
