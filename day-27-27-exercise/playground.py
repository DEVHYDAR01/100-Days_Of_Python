# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
#
# print(add(2, 3, 4, 110))

# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)

# def button_clicked():
#     get_val = enter.get()
#     my_label["text"] = get_val
#
#
# windows = Tk()
# windows.minsize(width=500, height=300)
# windows.title("My First GUI")
#
# my_label = Label(text="I am label", font=("arial", 8, "bold"))
# my_label["text"] = "New Text"
# my_label.grid(column=0, row=0)
#
# # button
# button = Button(text="Click me", command=button_clicked)
# button.grid(column=1, row=1)
#
# button = Button(text="new button", command=button_clicked)
# button.grid(column=2, row=0)
#
# enter = Entry(width=10)
# enter.grid(column=3, row=2)