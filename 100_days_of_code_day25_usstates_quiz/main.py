import turtle
from state import State, df

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

answer = screen.textinput("Guess the State", "What's another state?")
states_list = df.state.to_list()
states_list_lower = []
for state in states_list:
    states_list_lower.append(state.lower())

state = State()

while len(state.found_states) < len(states_list):
    if answer.lower() == 'off':
        state.game_over()
        break

    if answer.lower() in states_list_lower and answer.lower() not in state.found_states:
        state.create_state(answer.title())
        state.found_states.append(answer)

    answer = screen.textinput(f"{len(state.found_states)}/{len(states_list)} States Correct", "What's another state?")

state.game_over()

screen.exitonclick()

state.to_learn()
