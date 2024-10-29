import tkinter

windows = tkinter.Tk()
windows.minsize(width=500, height=300)
windows.title("My First GUI")

my_label = tkinter.Label(text="I am label", font=("arial", 8, "bold"))
my_label.pack()



windows.mainloop()