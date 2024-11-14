from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_WORD = "French"
ENGLISH_WORD = "English"

windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    df = pandas.read_csv("./words_to_learn.csv")
    list_of_dicts = df.to_dict(orient="records")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")
    list_of_dicts = df.to_dict(orient="records")
get_random_dict = {}

# function to flip the card
def flip_card():
    canvas.itemconfig(canvas_image, image=canvas_image_back)
    canvas.itemconfig(title_canvas, text=f"{ENGLISH_WORD}", fill="white")
    canvas.itemconfig(word_canvas, text=f"{get_random_dict[ENGLISH_WORD]}", fill="white")


# function to read csv and generate random words
def next_card():
    global get_random_dict, flip_timer
    windows.after_cancel(flip_timer)
    get_random_dict = random.choice(list_of_dicts)
    canvas.itemconfig(title_canvas, text=f"{FRENCH_WORD}", fill="black")
    canvas.itemconfig(word_canvas, text=f"{get_random_dict[FRENCH_WORD]}", fill="black")
    canvas.itemconfig(canvas_image, image=canvas_image_front)
    flip_timer = windows.after(3000, flip_card)


def is_known():
    list_of_dicts.remove(get_random_dict)
    table = pandas.DataFrame(list_of_dicts)
    table.to_csv("data/words_to_learn.csv", index=False)
    next_card()

flip_timer = windows.after(3000, flip_card)

# creating flashcard with canvas
canvas = Canvas(width=800, height=526)
canvas_image_front = PhotoImage(file="./images/card_front.png")
canvas_image_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=canvas_image_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_canvas = canvas.create_text(400, 150, text=f"title", font=("Ariel", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text=f"word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
my_image_correct = PhotoImage(file="./images/right.png")
correct_button = Button(image=my_image_correct, highlightthickness=0, command=is_known)
correct_button.grid(row=1, column=1)

my_image_wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=my_image_wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

windows.mainloop()