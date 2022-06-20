from turtle import Turtle
SCOREBOARD_POSITION = (0, 240)
ALIGNMENT = 'center'
FONT = ('Courier', 32, 'bold')
GAME_OVER_FONT = ('Courier', 26, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(SCOREBOARD_POSITION)
        self.write(f"Score: {self.l_score} - {self.r_score}", align=ALIGNMENT, font=FONT)

    def update_l_score(self):
        self.clear()
        self.l_score += 1
        self.write(f"Score: {self.l_score} - {self.r_score}", align=ALIGNMENT, font=FONT)

    def update_r_score(self):
        self.clear()
        self.r_score += 1
        self.write(f"Score: {self.l_score} - {self.r_score}", align=ALIGNMENT, font=FONT)

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"GAME OVER. Winner is {winner}!", align=ALIGNMENT, font=GAME_OVER_FONT)
