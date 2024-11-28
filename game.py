import random

import streamlit as st


def app():
    st.title("Guessing Game")

    # State management for the random number
    if "random_number" not in st.session_state:
        st.session_state.random_number = random.randint(1, 100)

    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    if "game_data" not in st.session_state:
        st.session_state.game_data = []  # To store game statistics

    st.write("I have selected a number between 1 and 100. Can you guess it?")

    user_guess = st.number_input(
        "Enter your guess:", min_value=1, max_value=100, step=1, format="%d"
    )
    submit = st.button("Submit Guess")

    if submit:
        st.session_state.attempts += 1
        if user_guess < st.session_state.random_number:
            st.warning("Too low! Try again.")
        elif user_guess > st.session_state.random_number:
            st.warning("Too high! Try again.")
        else:
            st.success(
                f"Correct! You guessed the number in {st.session_state.attempts} attempts."
            )
            # Record the game statistics
            game_num = len(st.session_state.game_data) + 1
            st.session_state.game_data.append((game_num, st.session_state.attempts))

            # Reset for a new game
            st.session_state.last_attempts = st.session_state.attempts
            st.session_state.random_number = random.randint(1, 100)
            st.session_state.attempts = 0
