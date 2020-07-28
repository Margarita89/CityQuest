"""

Store consts related to questions' engine

"""
from enum import Enum, auto


class QuestionEntities(Enum):
    question = auto()
    answer = auto()
    hints = auto()
    guidance = auto()
    position = auto()
    image = auto()


class Cities(Enum):
    empty = 'None'
    new_york = 'New York'
    san_francisco = 'San Francisco'


IMAGE_BASE_NAME_NEW_YORK = 'Images/New_York_map_'

NEW_YORK_QUESTION_DATA = {
    1: {
        QuestionEntities.guidance:
            'Please, start at the entrance gate of the Central Park Zoo',
        QuestionEntities.position: '40.767660, -73.971271',
        QuestionEntities.image: IMAGE_BASE_NAME_NEW_YORK + '1',
        QuestionEntities.question: 'When its precursor, a menagerie, was '
                                   'founded?',
        QuestionEntities.answer: '1864',
        QuestionEntities.hints: ['18..', '18.4']},
    2: {
        QuestionEntities.guidance:
            'Please, move to 2..',
        QuestionEntities.position: '40.767660, -73.971271',
        QuestionEntities.image: IMAGE_BASE_NAME_NEW_YORK + '2',
        QuestionEntities.question: 'Four thousand dollars towards the funding'
                                   ' of the statue was raised at'
                                   ' a benefit of which performance?',
        QuestionEntities.answer: 'Julius Caesar',
        QuestionEntities.hints: ['J..... C.....', 'Julius C.....']},
    3: {
        QuestionEntities.guidance:
            'Please, move to 3..',
        QuestionEntities.position: '40.767660, -73.971271',
        QuestionEntities.image: IMAGE_BASE_NAME_NEW_YORK + '3',
        QuestionEntities.question: 'For which anniversary of his arrival in '
                                   'the Americas it was donated?',
        QuestionEntities.answer: '400th',
        QuestionEntities.hints: ['4..th', '40.th']},
    4: {
        QuestionEntities.guidance:
            'Please, move to 4..',
        QuestionEntities.position: '40.767660, -73.971271',
        QuestionEntities.image: IMAGE_BASE_NAME_NEW_YORK + '4',
        QuestionEntities.question: 'What is the name of the fountain statue?',
        QuestionEntities.answer: 'Angel of the Waters',
        QuestionEntities.hints: ['Angel of the ......',
                                 'Angel of the W.....']},
    5: {
        QuestionEntities.guidance:
            'Please, move to 5..',
        QuestionEntities.position: '40.767660, -73.971271',
        QuestionEntities.image: IMAGE_BASE_NAME_NEW_YORK + '5',
        QuestionEntities.question: 'Where Alice is pictured sitting?',
        QuestionEntities.answer: 'mushroom',
        QuestionEntities.hints: ['m.......', 'm......m']},
    6: {
        QuestionEntities.guidance:
            'Please, move to 6..',
        QuestionEntities.position: '40.767660, -73.971271',
        QuestionEntities.image: IMAGE_BASE_NAME_NEW_YORK + '6',
        QuestionEntities.question: 'What means belvedere in Italian?',
        QuestionEntities.answer: 'beautiful view',
        QuestionEntities.hints: ['b........ v...', 'beautiful v...']},
    #7: {
    #    QuestionEntities.question: 'Where do most of the park\'s turtles '
    #                               'live?',
    #    QuestionEntities.answer: 'Turtle Pond',
    #    QuestionEntities.hints: ['T..... P...', 'Turtle P...']}
}

SAN_FRANCISCO_QUESTION_DATA = {
    1: {
        QuestionEntities.question: 'SF1?',
        QuestionEntities.answer: 'SF1_1',
        QuestionEntities.hints: ['SF_1_1_1', 'SF_1_1_2']},
    2: {
        QuestionEntities.question: 'SF2',
        QuestionEntities.answer: 'Julius Caesar',
        QuestionEntities.hints: ['J..... C.....', 'Julius C.....']}
}

CITY_TO_DATA = {
    Cities.new_york: NEW_YORK_QUESTION_DATA,
    Cities.san_francisco: SAN_FRANCISCO_QUESTION_DATA
}


class UserDecisions(Enum):
    hint = 'hint'
    returning = 'back'
    skip = 'skip'


class QuestionStates(Enum):
    question = 'question'
    select_next_action_after_wrong_answer = 'select_next_action_after_wrong_answer'
    final = 'final'

    hidden_analyze_answer = 'hidden_analyze_answer'
    hidden_user_decision = 'hidden_user_decision'


map_state_to_sentence = {
    QuestionStates.select_next_action_after_wrong_answer.value:
        'Sorry, wrong answer. Please, enter 1 of the 3 following options:\n'
        ' - hint (will give you a hint to the question)\n '
        ' - back (will bring you back to the question)\n '
        ' - skip (will allow you to skip this question)\n',
        'no_more_hints': 'Sorry, there are no more hints..'
}


class Triggers(Enum):
    user_answers = 'user_answers'
    go_to_next_question = 'go_to_next_question'
    incorrect_answer = 'incorrect_answer'
    user_decides = 'user_decides'
    returning = 'back'
    skip = 'skip'
    hint = 'hint'
    move_to_final = 'move_to_final'
