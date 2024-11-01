from tkinter import *

windows = Tk()
windows.title("Mile to Km Converter")
windows.minsize(width=150, height=100)
windows.config(padx=50, pady=50)


def cal_miles_to_km():
    get_miles = int(input_text.get())
    km = get_miles * 1.60943
    answer_label.config(text=round(km))


equal_to_label = Label()
equal_to_label.config(text="is equal to")
equal_to_label.grid(column=0, row=1)

answer_label = Label()
answer_label.config(text="0")
answer_label.grid(column=1, row=1)

miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label()
km_label.config(text="Km")
km_label.grid(column=2, row=1)

input_text = Entry(width=10)
input_text.insert(END, "0")
input_text.grid(column=1, row=0)

calculate_button = Button()
calculate_button.config(text="Calculate", command=cal_miles_to_km)
calculate_button.grid(column=1, row=2)




windows.mainloop()