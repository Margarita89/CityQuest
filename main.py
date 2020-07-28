import streamlit as st
import streamlit.ReportThread as ReportThread

from question_engine.question_engine import Quiz
from question_engine.questions_const import CITY_TO_DATA, Cities, QuestionStates
from curret_state import State

"""
# City Quest - NLP-powered game to explore the city
"""

cities = {'city list': [city.value for city in Cities]}

user_answer = ''
#@st.cache
def get_quiz(city_name: str):
    if city_name == Cities.empty.value:
        return None
    try:
        quiz = Quiz(questions_data=CITY_TO_DATA[Cities(city_name)])
    except ValueError as exc:
        print(f'Bad city name: {city_name}')
    return quiz


def get_layout():
    print(f'quiz state 1= {State.get_quiz_state()}')
    State.p_counter += 1
    arr = {'1': '1. You can choose 1 city from several options on the left sidebar',
           '2': '2. There will be 2 options: ',
           '2.1': '- to play with NLP (which means that questions will be generated from text in Wikipedia',
           '2.2': '- to play with human-written questions',
           '3': '3. There will be 6 questions and 2 hints for each question. You can always skip the question',
           '4': '4. The score will be calculated\n'}

    selected_city = st.sidebar.selectbox(
                    'In which city do you want to play?',
                    cities['city list'])

    #'You selected:', selected_city

    if selected_city != State.current_city:
        State.quiz = get_quiz(city_name=selected_city)
        State.current_city = selected_city

    print(f'quiz state 2= {State.get_quiz_state()} quiz={State.quiz}')
    if State.quiz is not None:

        print(f'enter')

        user_answer = st.sidebar.text_input("Your answer:", '')
        if user_answer != State.current_answer:
            State.current_answer = user_answer
            print('ha', State.get_quiz_state(), QuestionStates.question, QuestionStates.select_next_action_after_wrong_answer)
            # if the user answers the question
            if State.get_quiz_state() == QuestionStates.question.value:
                State.quiz.user_answers(user_answer=user_answer)
                print('enter question')
            # if the user inputs 1 of the options as an answer (currently: skip, hint, back)
            elif State.get_quiz_state() == QuestionStates.select_next_action_after_wrong_answer.value:
                State.quiz.check_and_trigger_user_decision(user_decision=user_answer)
                print('enter wrong answer')

        if State.quiz.correct_asnwer:
            st.subheader(State.quiz.correct_asnwer)

        # print Location
        if State.get_quiz_state() == QuestionStates.question.value:
            # print Location Num
            cur_location = 'Location ' + str(State.quiz.current_question_num)
            st.subheader(cur_location)
            # print location
            st.text(State.quiz.get_guidance())
            cur_map = 'Images/New_York_map_' + str(State.quiz.current_question_num) + '.png'
            st.image(cur_map, use_column_width=True)

        # print Question Num
        cur_question_num = 'Question ' + str(State.quiz.current_question_num)
        st.subheader(cur_question_num)
        # always print question
        st.text(State.quiz.get_current_question())


        # print all hints asked until now if any
        for hint_num, hint in enumerate(State.quiz.get_current_hints()):
            st.subheader(f"Hint {hint_num + 1}: {hint}")
        # print get_state_message if any
        st.subheader(State.quiz.get_state_message())

        print(State.quiz.get_state_message())

        print(f'user_ans={user_answer}')
        print(f'quiz state 3= {State.get_quiz_state()}, user_answer={user_answer}')
        if user_answer != '':
            print(f'quiz state 4= {State.get_quiz_state()}, user_answer={user_answer}')

    if selected_city == Cities.empty.value:
        st.header(f'Here\'s how it works: {State.p_counter}')
        for elem in arr.values():
            st.markdown(elem)
        st.subheader('Here you can see a New York map with 6 stars that correspond to real locations of the questions')

        st.image('Images/New_York_map.png', use_column_width=True)


get_layout()
