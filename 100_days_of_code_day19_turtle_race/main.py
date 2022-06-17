import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Creating turtles and move them to start positions
for i in range(6):
    distance = -40.0
    pam = Turtle(shape='turtle')
    pam.penup()
    pam.speed(5)
    pam.color(colors[i])
    pam.goto(-230, 100 + distance * i)

# Drawing a finish line
michael = Turtle()
michael.hideturtle()
michael.penup()
michael.goto(220, -120)
michael.setheading(90)
michael.pendown()
michael.forward(240)


def game():
    race_is_on = True
    while race_is_on:
        results = []
        for j in range(6):
            jim = turtle.turtles()[j]
            jim.speed(2)
            jim.goto(jim.xcor() + random.randint(8, 15), jim.ycor())
            results.append([jim.fillcolor(), jim.xcor()])
            if jim.xcor() >= 220:
                race_is_on = False
                print(results)
                print(f"The winner is {jim.fillcolor()} turtle!")
                if jim.fillcolor() == user_bet:
                    print("You win!")
                else:
                    print("You lose.")
                break


# Starting a game
turtle.listen()
turtle.onkey(fun=game, key='space')

screen.exitonclick()
