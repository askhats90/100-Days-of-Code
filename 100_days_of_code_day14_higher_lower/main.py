from game_data import data
from art import logo, vs
import random

score = 0
previous_score = 0
a, b = random.choice(data), random.choice(data)


def print_start():
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")


def set_user_choice():
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    return user_choice


def set_winner():
    if a['follower_count'] > b['follower_count']:
        winner = 'a'
    else:
        winner = 'b'
    return winner


def view_score():
    global score
    global previous_score
    global a
    global b
    previous_score = score
    if set_user_choice() == set_winner():
        score += 1
        print(f"You're right! Current score: {score}.")
        a = b
        b = random.choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        print("Game over.")


print(logo)
print_start()
view_score()
print("----------------------------")
while score > previous_score:
    print_start()
    view_score()
    print("----------------------------")
