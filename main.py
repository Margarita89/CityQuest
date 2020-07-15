import streamlit as st
import streamlit.ReportThread as ReportThread
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.


#st.title('My first app')
from question_engine.question_engine import Quiz
from question_engine.questions_const import CITY_TO_DATA, Cities
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
    st.header(f'Here\'s how it works: {State.p_counter}')
    arr = {'1': '1. You can choose 1 city from several options on the left sidebar',
           '2': '2. There will be 2 options: ',
           '2.1': '- to play with NLP (which means that questions will be generated from text in Wikipedia',
           '2.2': '- to play with human-written questions',
           '3': '3. There will be 6 questions and 2 hints for each question. You can always skip the question',
           '4': '4. The score will be calculated\n'}

    for elem in arr.values():
        st.markdown(elem)
    st.subheader('Here you can see a New York map with 6 stars that correspond to real locations of the questions')

    st.image('Images/New_York_map.png', use_column_width=True)

    selected_city = st.sidebar.selectbox(
        'In which city do you want to play?',
         cities['city list'])

    'You selected:', selected_city

    if selected_city != State.current_city:
        State.quiz = get_quiz(city_name=selected_city)
        State.current_city = selected_city

    print(f'quiz state 2= {State.get_quiz_state()} quiz={State.quiz}')
    if State.quiz is not None:

        print(f'enter')

        user_answer = st.sidebar.text_input("Your answer:", '')
        if user_answer != State.current_answer:
            State.current_answer = user_answer
            State.quiz.user_answers(user_answer=user_answer)

        st.sidebar.text(State.quiz.state)
        st.sidebar.text(State.quiz.get_state_message())

        print(f'user_ans={user_answer}')
        print(f'quiz state 3= {State.get_quiz_state()}, user_answer={user_answer}')
        if user_answer != '':
            print(f'quiz state 4= {State.get_quiz_state()}, user_answer={user_answer}')

get_layout()
