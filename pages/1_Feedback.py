import streamlit as st

st.title("Share feedback")

with st.sidebar:
    st.markdown("This page allows you to share feedback on the Chatbot.")

with st.form("myform"):
    topic_text = st.text_input("Enter feeback:", "")
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.info("Thank you for your feedback!")	
