from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH FEATURE ------------------------------- #
def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Data File Found", message="Data Not Found")
    else:
        website = website_entry.get()
        try:
            email = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showinfo(title="No Data Found", message="No details for the website exists")
        else:
            messagebox.showinfo(title="Data Found", message=f"{email}\n{password}")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website)==0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: "
                                                              f"{password}\nIs it ok to save?")
        if is_ok:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Project Manager")
window.config(padx=50, pady=20)
canvas = Canvas(width=200, height=200)
pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "zubsyeda@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)

# Buttons
search_button = Button(text="Search", width=10, command=search)
search_button.grid(row=1, column=2)
generate_button = Button(text="Generate Password", command=gen_password, width=10)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=32, command=save)
add_button.grid(column=1, row=4, columnspan=2)

















window.mainloop()