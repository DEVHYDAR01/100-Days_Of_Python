from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_paddle = 0
        self.r_paddle = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_paddle, align="center", font=("courier", 60, "bold"))
        self.goto(100, 200)
        self.write(self.r_paddle, align="center", font=("courier", 60, "bold"))

    def l_paddle_score(self):
        self.clear()
        self.l_paddle += 1
        self.update_score()

    def r_paddle_score(self):
        self.clear()
        self.r_paddle += 1
        self.update_score()