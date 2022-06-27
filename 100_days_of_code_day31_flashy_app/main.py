from tkinter import *
import pandas
import random

# ------------------------- CONSTANTS ---------------------------------
BACKGROUND_COLOR = "#B1DDC6"
card_num = 0
flip_timer = None

# ------------------------- IMPORT DATA ---------------------------------
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
    data_dict = data.to_dict()
    new_index = len(data_dict['French'])
else:
    data_dict = data.to_dict()
    new_index = len(data_dict['French'])


def random_card():
    global card_num
    keys = list(data_dict['French'].keys())
    card_num = random.choice(keys)


# ------------------------- BUTTON COMMANDS ---------------------------------

def remove_card():
    data_dict['French'].pop(card_num)
    data_dict['English'].pop(card_num)
    window.after_cancel(flip_timer)
    create_card()


def add_card():
    global new_index
    data_dict['French'].update({new_index: data_dict['French'][card_num]})
    data_dict['English'].update({new_index: data_dict['English'][card_num]})
    new_index += 1
    data_dict['French'].pop(card_num)
    data_dict['English'].pop(card_num)
    window.after_cancel(flip_timer)
    create_card()


# ------------------------- FLIP MECHANICS ---------------------------------
def create_card():
    global flip_timer
    random_card()
    create_fr_card(card_num)
    flip_timer = window.after(3000, create_en_card, card_num)

    print(data_dict)
    print(card_num, data_dict['French'][card_num], data_dict['English'][card_num])
    print(len(data_dict['French']), len(data_dict['English']))
    print(new_index)
    print("----------------------")


def create_fr_card(number):
    new_fr_word = data_dict['French'][number]
    canvas.itemconfig(lang, text='French', fill='black')
    canvas.itemconfig(word, text=new_fr_word, fill='black')
    canvas.itemconfig(image, image=card_front_img)


def create_en_card(number):
    new_en_word = data_dict['English'][number]
    canvas.itemconfig(lang, text='English', fill='white')
    canvas.itemconfig(word, text=new_en_word, fill='white')
    canvas.itemconfig(image, image=card_back_img)


# ------------------------- UI SETUP ---------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263)
lang = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 270, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right_img, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=add_card)
wrong_button.grid(row=1, column=0)

create_card()

window.mainloop()

print("EXIT THE APP!!!")
new_data = pandas.DataFrame(data_dict)
new_data.to_csv('data/words_to_learn.csv', index=False)
