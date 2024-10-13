from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.content = int(file.read())
        self.high_score = self.content
        print(self.high_score)
        self.goto(0, 280)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score} HIGHSCORE: {self.high_score}",
                   move=False, align="center", font=('Arial', 8, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
