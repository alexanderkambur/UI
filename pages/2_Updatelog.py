import streamlit as st

# Hide the Streamlit gradient bar
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

st.title("What's new?")

with st.sidebar:
    st.markdown("This page provides a high-level overview of the updates made to the Chatbot.")