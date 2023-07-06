import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()

    if turtle.refresh():
        scoreboard.incremenentScore()
        car.increase_speed()

    for i in car.car_list:
        if turtle.distance(i) < 25:
            scoreboard.game_over()
            
            game_is_on = False



screen.exitonclick()
