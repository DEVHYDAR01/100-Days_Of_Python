from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed_increase = 0.1

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=1.9, stretch_wid=0.95)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-300 - 50, 300 - 50))
            self.cars.append(new_car)

    def car_movement(self):
        for car in self.cars:
            car.fd(STARTING_MOVE_DISTANCE)

    def speed_add(self):
        self.speed_increase *= 0.9
