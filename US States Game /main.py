import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
correct_guesses = []
states_list = data.state.to_list()
missed = []

while score != 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name").title()
    if answer_state == "Exit":
        missed = [state for state in states_list if state not in correct_guesses]
        new_data = pandas.DataFrame(missed)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        if answer_state not in correct_guesses:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
            score += 1
            correct_guesses.append(answer_state)

print(correct_guesses)
