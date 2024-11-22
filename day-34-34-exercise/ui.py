from tkinter import *

import quiz_brain
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizzerInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.windows = Tk()
        self.windows.title("QUIZZLER")
        self.windows.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score = 0

        self.label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="haffa",
            font=("ariel", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        my_right_image = PhotoImage(file="./images/true.png")
        my_wrong_image = PhotoImage(file="./images/false.png")
        self.right_button = Button(image=my_right_image, bg=THEME_COLOR, command=self.right_answer)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=my_wrong_image, bg=THEME_COLOR, command=self.wrong_answer)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.text, text=q_text)

        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz!!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_answer(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def wrong_answer(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000, self.get_next_question)

