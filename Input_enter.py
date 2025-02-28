import streamlit as st

def input_enter():
    prompt = st.text_input("Enter the text ")
    st.session_state["prompt"] = prompt