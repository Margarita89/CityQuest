"""
Class that represents the current state of the application
"""
from question_engine.questions_const import QuestionStates


class State:
    p_counter = 1
    current_city = ''
    current_answer = ''
    quiz = None

    @staticmethod
    def get_quiz_state() -> str:
        if State.quiz:
            return State.quiz.state
        return 'No quiz'

    @staticmethod
    def get_answer(ans: str):
        if ans != '' and State.quiz.state == QuestionStates.question.value:
            print(f'update')
            State.quiz.user_answers(user_answer=ans)

