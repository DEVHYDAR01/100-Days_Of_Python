from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for char in range(randint(8, 10))]
    symbols_list = [choice(symbols) for sym in range(randint(2, 4))]
    numbers_list = [choice(numbers) for num in range(randint(2, 4))]

    password_list = letter_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    get_web_input = website_input.get()
    get_email_input = emailuser_input.get()
    get_pass_input = password_input.get()
    new_data = {
        get_web_input: {
            "email": get_email_input,
            "password": get_pass_input
        }
    }

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        with open("./data.json", mode="r") as pass_file:
            data = json.load(pass_file)
            data.update(new_data)
        with open("./data.json", mode="w") as pass_file:
            json.dump(data, pass_file, indent=4)




        website_input.delete(0, len(get_web_input))
        password_input.delete(0, len(get_pass_input))



# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
picture = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=picture)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

emailuser_label = Label(text="Email/Username:")
emailuser_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

emailuser_input = Entry(width=35)
emailuser_input.grid(row=2, column=1, columnspan=2)
emailuser_input.insert(END, "aliyuahmaad60@gmail.com")

password_input = Entry(width=18)
password_input.grid(row=3, column=1)

# buttons
generate_button = Button(text="Generate Password", width=13, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)


windows.mainloop()