from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_QUESTION = ('Arial', 20, 'italic')
FONT_SCORE = ('Arial', 14, 'normal')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz App')
        self.window.config(bg=THEME_COLOR, pady=20)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question here",
            font=FONT_QUESTION,
            fill=THEME_COLOR
        )

        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')

        self.true_bt = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_bt.grid(row=2, column=0)

        self.false_bt = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_bt.grid(row=2, column=1)

        self.score_lb = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white', font=FONT_SCORE)
        self.score_lb.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_lb.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The end of quiz.")
            self.true_bt.config(state='disabled')
            self.false_bt.config(state='disabled')

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
