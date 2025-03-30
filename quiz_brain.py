from debugpy.common.timestamp import current


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.quiz_running = True

    def still_has_question(self):
        return self.question_number < len(self.question_list) and self.quiz_running == True


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False)")
        if user_answer == "off":
            self.quiz_running = False
            print("End quiz")
        else:
            self.check_answer(user_answer, current_question.answer)
            print(f"Your score is {self.score}/{self.question_number}")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"Correct answer is {correct_answer}.")