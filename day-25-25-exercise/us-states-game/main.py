import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

correct_answers = []

score = 0
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{score}/50 State correct",
                                    prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        learning_states = [state_list[guess] for guess in range(50) if not state_list[guess] in correct_answers]
        learning_states_dict = {
            "States": learning_states
        }
        df = pandas.DataFrame(learning_states_dict)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        score += 1
        correct_answers.append(answer_state)
        answer_row = data[data.state == answer_state]
        x_coordinate = int(answer_row.x)
        y_coordinate = int(answer_row.y)
        writer_and_goto = turtle.Turtle()
        writer_and_goto.penup()
        writer_and_goto.hideturtle()
        writer_and_goto.goto(x=x_coordinate, y=y_coordinate)
        writer_and_goto.write(arg=answer_state, align='center', font=('Arial', 8, 'normal'))



