
from transitions import Machine as Machine

from question_engine.questions_const import QuestionStates, Triggers, \
    UserDecisions, QuestionEntities, map_state_to_sentence


class Quiz:
    # Define states
    states = [state.value for state in QuestionStates]

    def __init__(self, questions_data):
        self.questions_data = questions_data
        self.additional_message = ''
        self.user_hint_counter = 0
        self.current_question_num = 1
        self.total_questions = len(self.questions_data)
        self.correct_asnwer = ''

        # Initialize the state machine
        self.machine = Machine(
            model=self,
            states=Quiz.states,
            initial=QuestionStates.question.value)

        # When user answers move from question 1 to analyzing answer
        self.machine.add_transition(
            trigger=Triggers.user_answers.value,
            source=QuestionStates.question.value,
            dest=QuestionStates.hidden_analyze_answer.value,
            after='get_user_answer')

        # If answer is correct move from question 1 to question 2
        self.machine.add_transition(
            trigger=Triggers.go_to_next_question.value,
            source=QuestionStates.hidden_analyze_answer.value,
            dest=QuestionStates.question.value)

        # If answer is incorrect move from question 1 to state 'select'
        self.machine.add_transition(
            trigger=Triggers.incorrect_answer.value,
            source=QuestionStates.hidden_analyze_answer.value,
            dest=QuestionStates.select_next_action_after_wrong_answer.value)

        # When user decides where to move from analyzing answer
        self.machine.add_transition(
            trigger=Triggers.user_decides.value,
            source=QuestionStates.select_next_action_after_wrong_answer.value,
            dest=QuestionStates.hidden_user_decision.value,
            after='get_user_decision')

        # Return from state 'select' back to question 1
        self.machine.add_transition(
            trigger=Triggers.returning.value,
            source=QuestionStates.hidden_user_decision.value,
            dest=QuestionStates.question.value)

        # Skip this question from state 'select' to question 2
        self.machine.add_transition(
            trigger=Triggers.skip.value,
            source=QuestionStates.hidden_user_decision.value,
            dest=QuestionStates.hidden_analyze_answer.value,
            after='move_to_next_question')

        # Choose hint and move from state 'select' back to question 1 with a hint
        self.machine.add_transition(
            trigger=Triggers.hint.value,
            source=QuestionStates.hidden_user_decision.value,
            dest=QuestionStates.question.value)

        # Move to state 'final' if there are no more questions
        self.machine.add_transition(
            trigger=Triggers.move_to_final.value,
            source=QuestionStates.hidden_analyze_answer.value,
            dest=QuestionStates.final.value)

    def get_user_answer(self, user_answer):
        self.additional_message = ''
        #self.correct_asnwer = ''
        correct_answer = self.questions_data[self.current_question_num][
            QuestionEntities.answer]
        if user_answer == correct_answer:
            self.correct_asnwer = 'Correct answer. Congratulations!'
            self.move_to_next_question()
        else:
            self.correct_asnwer = ''
            self.incorrect_answer()

    def get_user_decision(self, user_decision: UserDecisions) -> None:
        if user_decision == UserDecisions.hint.value:
            hints_array = self.questions_data[self.current_question_num][
                QuestionEntities.hints]
            hints_amount = len(hints_array)
            if self.user_hint_counter < hints_amount:
                #self.additional_message = hints_array[self.user_hint_counter]
                self.user_hint_counter += 1
            else:
                self.additional_message = map_state_to_sentence['no_more_hints']
            self.hint()

        elif user_decision == UserDecisions.skip.value:
            self.skip()
        elif user_decision == UserDecisions.returning.value:
            self.back()

    def get_state_message(self):
        if self.state == QuestionStates.question.value:
            return self.additional_message
        if self.state == QuestionStates.select_next_action_after_wrong_answer.value:
            return map_state_to_sentence[
                QuestionStates.select_next_action_after_wrong_answer.value]

    def move_to_next_question(self):
        if self.current_question_num < self.total_questions:
            self.current_question_num += 1
            self.user_hint_counter = 0
            self.go_to_next_question()
        else:
            self.move_to_final()

    def get_current_question(self):
        return self.questions_data[self.current_question_num][
            QuestionEntities.question]

    def get_current_hints(self):
        return self.questions_data[self.current_question_num][
                   QuestionEntities.hints][:self.user_hint_counter]

    def check_and_trigger_user_decision(self, user_decision):
        if user_decision in [Triggers.returning.value, Triggers.hint.value,
                             Triggers.skip.value]:
            self.user_decides(user_decision=user_decision)

    def get_guidance(self):
        return self.questions_data[self.current_question_num][
            QuestionEntities.guidance]
