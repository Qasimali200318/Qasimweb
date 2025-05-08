import random
import streamlit as st
import pandas as pd
import time

def response_generator():
    response = random.choice(

        [
"Hey!,  There! Need help?  ",
"Hello!, what's up?  ",
"Contact on , 03151103997 ",
"Email, Devqasimali75@gmail.com",
"(qasim Ali) , A Student in icma currenlty doiong CMA he is 21 year ol and he is aslo complete Advance diploma in Software Engineering 1.5 year experience in E-commerc",





        ]
    )

    for word in response.split():
        yield word + "  "
        time.sleep(0.05) 
st.title("Chat with us")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input(" Any Question "):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
     st.markdown(prompt)
    with st.chat_message("assistant"):
         response = st.write_stream(response_generator())
    
    
    st.session_state.messages.append({"role": "user", "content": response})