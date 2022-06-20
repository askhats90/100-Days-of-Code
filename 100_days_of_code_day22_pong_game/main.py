from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

STARTING_POSITIONS = [(350, 0), (-350, 0)]
x_distance, y_distance = 10, 10
sleep_time = 0.1


r_paddle = Paddle(STARTING_POSITIONS[0])
l_paddle = Paddle(STARTING_POSITIONS[1])
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.up, key='Up')
screen.onkey(fun=r_paddle.down, key='Down')
screen.onkey(fun=l_paddle.up, key='w')
screen.onkey(fun=l_paddle.down, key='s')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    ball.move(x_distance, y_distance)

    # Check if the ball collides with upper or lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        y_distance *= -1

    # Check if the ball collides with either of paddles
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        x_distance *= -1
        if sleep_time > 0.01:
            sleep_time -= 0.01

    # Check if Rudy misses the ball
    if ball.xcor() > 380:
        ball.refresh()
        sleep_time = 0.1
        x_distance *= -1
        scoreboard.update_l_score()
        if scoreboard.l_score >= 6:
            game_is_on = False
            scoreboard.game_over('Lewis')

    # Check if Lewis misses the ball
    if ball.xcor() < -380:
        ball.refresh()
        sleep_time = 0.1
        x_distance *= -1
        scoreboard.update_r_score()
        if scoreboard.r_score >= 6:
            game_is_on = False
            scoreboard.game_over('Rudy')

screen.exitonclick()
