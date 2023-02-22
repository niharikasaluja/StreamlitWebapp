import streamlit as st
import pandas as pd

#st.set_page_config(page_title="Stock Price", page_icon="chart_with_upwards_trend", layout="centered", initial_sidebar_state = "auto")

st.write("""
# NLP Question Answer
""")
Question = st.write("""
## What aspect of the shade should be considered while covering a wide window with a motorized shade?
""")
Answer = st.text_input('Answer:')


if st.button('Check Answer'):
    if Answer == "A light weight shade":
        st.write("Correct")
    else:
        st.write("Incorrect")


