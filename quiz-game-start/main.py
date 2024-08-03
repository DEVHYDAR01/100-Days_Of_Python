from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_dictionary = i
    get_text = question_dictionary["text"]
    get_answer = question_dictionary["answer"]
    question = Question(get_text, get_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz.next_question()