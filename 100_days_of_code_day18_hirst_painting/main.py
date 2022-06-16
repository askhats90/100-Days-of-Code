import turtle as t
from turtle import Screen
import random
import colorgram

colors = colorgram.extract('image.jpg', 100)
colors_list = []

for i in colors:
    color = (i.rgb.r, i.rgb.g, i.rgb.b)
    colors_list.append(color)

colors_list = colors_list[4:]

t.colormode(255)
pam = t.Turtle()
pam.speed('fastest')
pam.penup()
pam.hideturtle()


def draw_dots():
    for j in range(9):
        pam.dot(20, random.choice(colors_list))
        pam.forward(70)
    pam.dot(20, random.choice(colors_list))


def move_left():
    pam.left(90)
    pam.forward(70)
    pam.left(90)
    pam.forward(630)
    pam.setheading(0)


pam.setposition(-400, -300)

for row in range(9):
    draw_dots()
    move_left()
draw_dots()

screen = Screen()
screen.exitonclick()
