from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.x_coordinates = [(0, 0), (-20, 0), (-40, 0)]
        self.new_snake = []
        self.create()

    def create(self):
        for turtle in self.x_coordinates:
            self.add(turtle)

    def add(self, turtle):
        snake = Turtle(shape="square")
        snake.penup()
        snake.goto(turtle)
        snake.color("white")
        self.new_snake.append(snake)

    def reset(self):
        for seg in self.new_snake:
            seg.goto(1000, 1000)
        self.new_snake.clear()
        self.create()

    def extend(self):
        self.add(self.new_snake[-1].position())

    def up(self):
        if self.new_snake[0].heading() != DOWN:
            self.new_snake[0].setheading(UP)

    def down(self):
        if self.new_snake[0].heading() != UP:
            self.new_snake[0].setheading(DOWN)

    def left(self):
        if self.new_snake[0].heading() != RIGHT:
            self.new_snake[0].setheading(LEFT)

    def right(self):
        if self.new_snake[0].heading() != LEFT:
            self.new_snake[0].setheading(RIGHT)

    def move(self):
        for snake in range(len(self.new_snake) - 1, 0, -1):
            x_snake_cor = self.new_snake[snake - 1].xcor()
            y_snake_cor = self.new_snake[snake - 1].ycor()
            self.new_snake[snake].goto(x=x_snake_cor, y=y_snake_cor)
        self.new_snake[0].forward(MOVE_DISTANCE)
