from turtle import Turtle

FONT = ("Courier", 24, "bold")
POSITION = (-200, 250)
GAME_OVER_POSITION = (150, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def game_over(self):
        self.goto(GAME_OVER_POSITION)
        self.write("GAME OVER", align='center', font=FONT)
