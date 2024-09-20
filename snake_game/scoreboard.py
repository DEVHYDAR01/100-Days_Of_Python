from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.goto(0, 280)
        self.color("white")
        self.write(arg=f"score: {self.score}", move=False, align="center", font=('Arial', 8, 'normal'))
        self.hideturtle()

    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=('Arial', 8, 'normal'))

    def update_score(self):
        self.clear()
        self.score = self.score + 1
        self.write(arg=f"score: {self.score}", move=False, align="center", font=('Arial', 8, 'normal'))



