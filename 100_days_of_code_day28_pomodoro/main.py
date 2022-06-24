from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text='TIMER', fg=GREEN)
    tick_label.config(text='')
    canvas.itemconfig(timer_text, text=f"{WORK_MIN}:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def call_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    check_mark = '✔'
    check_mark_count = 0
    if reps in [1, 3, 5, 7]:
        countdown(work_secs)
        timer_label.config(text='WORK', fg=GREEN)
    elif reps in [2, 4, 6]:
        countdown(short_break_secs)
        timer_label.config(text='BREAK', fg=PINK)
        check_mark_count = int(reps / 2)
        tick_label.config(text=check_mark * check_mark_count)
    elif reps == 8:
        countdown(long_break_secs)
        timer_label.config(text='BREAK', fg=RED)
        check_mark_count = int(reps / 2)
        tick_label.config(text=check_mark * check_mark_count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global reps
    global timer

    minutes = str(count // 60 + 100)
    seconds = str(count % 60 + 100)
    canvas.itemconfig(timer_text, text=f"{minutes[1:]}:{seconds[1:]}")
    if count > 0:
        timer = window.after(50, countdown, count - 1)
    elif count == 0:
        call_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"{WORK_MIN}:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', command=call_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(row=2, column=2)

timer_label = Label(text='TIMER', font=(FONT_NAME, 48, 'bold'), bg=YELLOW, foreground=GREEN)
timer_label.grid(row=0, column=1)

tick_label = Label(font=(FONT_NAME, 18, 'bold'), bg=YELLOW, foreground=GREEN)
tick_label.grid(row=3, column=1)

window.mainloop()
