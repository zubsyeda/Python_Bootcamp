from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True




