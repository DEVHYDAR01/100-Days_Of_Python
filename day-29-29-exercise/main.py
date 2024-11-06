from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    get_web_input = website_input.get()
    get_email_input = emailuser_input.get()
    get_pass_input = password_input.get()

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="", message=f"These are the details entered:\nWebsite:{get_web_input}\n"
                                                         f"Password:{get_pass_input}\nIs it okay to save?")
        if is_ok:
            with open("./data.txt", mode="a") as pass_file:
                pass_file.write(f"\n{get_web_input} | {get_email_input} | {get_pass_input}")
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

# enteries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

emailuser_input = Entry(width=35)
emailuser_input.grid(row=2, column=1, columnspan=2)
emailuser_input.insert(END, "aliyuahmaad60@gmail.com")

password_input = Entry(width=18)
password_input.grid(row=3, column=1)

# buttons
generate_button = Button(text="Generate Password", width=13)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)


windows.mainloop()