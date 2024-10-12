from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = 0
        super().__init__()
        self.goto(0, 280)
        self.color("white")
        # self.write(arg=f"score: {self.score}", move=False, align="center", font=('Arial', 8, 'normal'))
        self.update_score()
        self.hideturtle()

    def score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score} HIGHSCORE: {self.high_score}", move=False, align="center", font=('Arial', 8, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1


