from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.move_count = STARTING_MOVE_DISTANCE
        self.car_list = []
        self.counter = 0

    def create_car(self):
        car = Turtle()
        car.penup()
        car.goto(300, random.randint(-250, 250))
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.setheading(180)
        self.car_list.append(car)

    def move(self):
        self.counter += 1
        if self.counter == 6:
            self.create_car()
            self.counter = 0

        for i in self.car_list:
            i.forward(self.move_count)

    def increase_speed(self):
        self.move_count += MOVE_INCREMENT
        self.move()

