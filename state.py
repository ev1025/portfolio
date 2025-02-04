import streamlit as st

def initialize_state():
    for key, value in {
        "year": None,
        "tab": None,
        "navi": None,
    }.items():
        if key not in st.session_state:
            st.session_state[key] = value