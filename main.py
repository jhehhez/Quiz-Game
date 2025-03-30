from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)

new_game = QuizBrain(question_list)
while new_game.still_has_question() and new_game.quiz_running:
    new_game.next_question()

print("You've completed the quiz")
print(f"Your final score is {new_game.score}/{new_game.question_number}")