from turtle import Turtle
# X_DISTANCE = 10   #20
# Y_DISTANCE = 10   #15
# MOVE_DISTANCE = (X_DISTANCE, Y_DISTANCE)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')

    def refresh(self):
        self.goto(0, 0)

    def move(self, x_distance, y_distance):
        self.goto(self.xcor() + x_distance, self.ycor() + y_distance)
