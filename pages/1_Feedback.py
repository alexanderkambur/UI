import streamlit as st

# Hide the Streamlit gradient bar
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

st.title("Share feedback")

with st.sidebar:
    st.markdown("This page allows you to share feedback on the Chatbot.")

with st.form("myform"):
    topic_text = st.text_input("Enter feedback:", "")
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.info("Thank you for your feedback!")
