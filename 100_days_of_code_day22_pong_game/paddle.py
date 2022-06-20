from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.color('white')
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
