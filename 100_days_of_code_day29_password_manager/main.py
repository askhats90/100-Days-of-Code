from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#F2F2F2"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list = [random.choice(letters) for letter in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for number in range(random.randint(2, 4))]

    password_list = char_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entry():
    new_site_entry = site_entry.get()
    new_username_entry = username_entry.get()
    new_password_entry = password_entry.get()

    if new_site_entry == '' or new_password_entry == '':
        messagebox.showinfo(title='Oops', message='One of the fields is empty')
    else:
        is_ok = messagebox.askokcancel(title=new_site_entry, message=f"Confirm username and password: \nUsername: {new_username_entry} \nPassword: {new_password_entry}")

        if is_ok:
            with open('data.txt', mode='a') as writer:
                writer.writelines(f"{new_site_entry} | {new_username_entry} | {new_password_entry}" + '\n')
                site_entry.delete(0, len(new_site_entry))
                password_entry.delete(0, END)
                site_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=35, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

site_label = Label(text='Website:', bg=YELLOW)
site_label.grid(row=1, column=0)

username_label = Label(text='Email / Username:', bg=YELLOW)
username_label.grid(row=2, column=0)

password_label = Label(text='Password:', bg=YELLOW)
password_label.grid(row=3, column=0)

site_entry = Entry(width=52)
site_entry.grid(row=1, column=1, columnspan=2, pady=3)
site_entry.focus()

username_entry = Entry(width=52)
username_entry.insert(0, 'someone@somewhere.com')
username_entry.grid(row=2, column=1, columnspan=2, pady=3)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, padx=2, pady=3)

pw_gen_button = Button(text='Generate Password', width=15, command=generate_password)
pw_gen_button.grid(row=3, column=2)

add_button = Button(text='Add', width=44, command=save_entry)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
