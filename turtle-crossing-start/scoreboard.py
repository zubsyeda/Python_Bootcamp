from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.score()

    def score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)
    def incremenentScore(self):
        self.level += 1
        self.clear()
        self.score()

    def game_over(self):
        self.clear()
        self.write("Game Over", align="center", font=FONT)