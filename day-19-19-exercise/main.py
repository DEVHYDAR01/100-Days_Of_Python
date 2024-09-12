from turtle import Turtle, Screen

screen = Screen()
# choose_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter your color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen.setup(width=500, height=400)
y_axis = [-70, -40, -10, 20, 50, 80]
for i in range(6):
    tess = Turtle(shape="turtle")
    tess.penup()
    tess.color(colors[i])
    tess.goto(x=-230, y=y_axis[i])

# print(choose_bet)

screen.exitonclick()