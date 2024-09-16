from turtle import Turtle


class Snake:

    def __init__(self):
        self.x_coordinates = [(0, 0), (-20, 0), (-40, 0)]
        self.new_snake = []
        for turtle in self.x_coordinates:
            snake = Turtle(shape="square")
            snake.penup()
            snake.goto(turtle)
            snake.color("white")
            self.new_snake.append(snake)

    def move(self):
        for snake in range(len(self.new_snake) - 1, 0, -1):
            x_snake_cor = self.new_snake[snake - 1].xcor()
            y_snake_cor = self.new_snake[snake - 1].ycor()
            self.new_snake[snake].goto(x=x_snake_cor, y=y_snake_cor)
        self.new_snake[0].forward(20)
        self.new_snake[0].right(90)
