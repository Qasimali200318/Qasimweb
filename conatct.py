import streamlit as st

import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZjMDYzZTA0MzM1MjZiNTUzNzUxMzIi_pc "

def is_vaild_email(email):
   email_pattern = r"^[a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-0-.]+$"
   return re.match(email_pattern,email) is not None
  



def conatct_form():
  with st.form("conatct_form"):
    name = st.text_input("First Name ")
    email = st.text_input("Email ")
    Message = st.text_area("Your message ")
    submit_button = st.form_submit_button("submit")

    if submit_button:
       if not WEBHOOK_URL:
          st.error(
             "Email service is not setup please try later",
          )
          st.stop()
       if not name:
          st.error(
             "please enter your name", 
          )
          st.stop()
       if not email:
          st.error(
             "please enter your email", 
          )
          st.stop()
       if not Message:
          st.error(
             "please enter your message",
          )
          st.stop()

       data = {"email": email, "name":name ,"Message":Message}
       response = requests.post(WEBHOOK_URL, json=data)

       if response.status_code ==200:
          st.success("Your message has been sent succesfully")
       else:
          st.error("there was an error loading your mesage")                     