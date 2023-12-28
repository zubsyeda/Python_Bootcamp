from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

global random_card
data_dict = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/KoreanFlashCards.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

print(data_dict)
random_card = random.choice(data_dict)

def new_card():
    global timer
    global random_card
    window.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=front_pic)
    canvas.itemconfig(word, fill="black")
    canvas.itemconfig(title, fill="black")
    random_card = random.choice(data_dict)
    canvas.itemconfig(title, text="Korean")
    canvas.itemconfig(word, text=random_card["Korean"])
    timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=back_pic)
    canvas.itemconfig(title, fill="white")
    canvas.itemconfig(word, fill="white")
    global random_card
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=random_card["English"])

def known_card():
    data_dict.remove(random_card)
    to_learn = pandas.DataFrame(data_dict)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_card()
    # try:
    #     known_data = pandas.read_csv("data/words_to_learn.csv")
    # except FileNotFoundError:
    #
    #     known_data_dict = data.to_dict(orient="records")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_pic = PhotoImage(file="images/card_back.png")
front_pic = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_pic)
canvas.grid(column=0, row=0, columnspan=2)

title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=new_card)
x_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, pady=50, padx=50, command=known_card)
right_button.grid(row=1, column=1)

new_card()





window.mainloop()