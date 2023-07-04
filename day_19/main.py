from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_back():
    tim.back(10)

def turn_anticlockwise():
    tim.left(10)

def turn_clockwise():
    tim.right(10)

def clear():
    tim.reset()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(turn_anticlockwise, "a")
screen.onkey(turn_clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()
