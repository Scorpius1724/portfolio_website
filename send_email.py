import smtplib, ssl
import streamlit as st
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = st.secrets["username"]
    password = st.secrets["password"]

    receiver = "helloworld21895@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

if __name__ == "__main__":
    send_email("abcd")