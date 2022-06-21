import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

sleep_time = 0.3
FINISH_LINE_Y = 250
player = Player()
scoreboard = Scoreboard()
car_list = []
for i in range(630):
    new_car = CarManager()
    car_list.append(new_car)

screen.listen()
screen.onkey(fun=player.move, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()

    # Check if player collides with top of the game box
    if player.ycor() > FINISH_LINE_Y:
        player.refresh()
        scoreboard.update()
        sleep_time *= 0.75

    # Check if player collides with a car
    for car in car_list:
        car.move()
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
