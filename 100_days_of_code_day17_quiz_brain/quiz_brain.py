class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}. {current_q.text} (True/False?): ")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print("You are right!")
        else:
            print("You are wrong.")

        print(f"Correct answer is: {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}.")
        print("\n")