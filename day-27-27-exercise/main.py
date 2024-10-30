from tkinter import *


def button_clicked():
    get_val = enter.get()
    my_label["text"] = get_val


windows = Tk()
windows.minsize(width=500, height=300)
windows.title("My First GUI")

my_label = Label(text="I am label", font=("arial", 8, "bold"))
my_label["text"] = "New Text"
my_label.pack()


# button
button = Button(text="Click me", command=button_clicked)
button.pack()

enter = Entry(width=10)
enter.pack()




windows.mainloop()