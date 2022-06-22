from turtle import Turtle
import pandas

FONT = ("Arial", 9, "normal")
GAME_OVER_FONT = ("Arial", 16, "bold")

df = pandas.read_csv('50_states.csv')


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.found_states = []

    def create_state(self, state):
        x_cor = df[df.state == state].x
        y_cor = df[df.state == state].y
        state_coordinates = (int(x_cor), int(y_cor))
        self.goto(state_coordinates)
        self.write(state, align='left', font=FONT)

    def game_over(self):
        self.goto(-150, 270)
        self.write(f"Congratulations! You know {len(self.found_states)} US states!", font=GAME_OVER_FONT)

    def to_learn(self):
        not_found_states = []
        for i in df.state.to_list():
            if i.lower() not in self.found_states:
                not_found_states.append(i)

        states_to_learn = pandas.DataFrame(not_found_states)
        states_to_learn.to_csv('States_to_learn.csv')
