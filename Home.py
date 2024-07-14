import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/title_image.png")

with col2:
    st.title("Swapnil Acharjee")
    content = ("""
    Greetings! I am Swapnil Acharjee. I am an engineering student, pursuing a B.Tech degree in Computer Science and Engineering (CSE).
    I am also a Python programmer. I've made this website as my portfolio.
    It showcases some of the projects that I've made using Python or other programming languages, along with their source codes.
    This website itself is also made entirely using Python and is one of my projects.
    If you find Python cool, or have any comments or questions regarding my projects, feel free to send a message through the "Contact Me" page. 
    """)
    st.info(content)


st.write(" ")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")


with col3:
    for index, row in df[:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[4:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")