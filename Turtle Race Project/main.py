from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle with win the rance? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

starting_x = -225
starting_y = -110
turtles = []

turtleNames = "turtle"
for i in colors:
    turtleName = turtleNames + "_" + i
    turtleName = Turtle(shape = "turtle")
    turtleName.color(i)
    turtleName.penup()
    starting_y += 30
    turtleName.goto(starting_x, starting_y)
    turtles.append(turtleName)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in turtles:
        if i.xcor() > 220:
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
        i.forward(random.randint(0, 10))


screen.exitonclick()
