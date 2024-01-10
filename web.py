import streamlit as st
import functions

todos = functions.get_todos()

st.title('My Todo Ap.p')
st.subheader('This is my todo app.')

for index, todo in enumerate(todos):
    st.checkbox(todo, key=index)

st.text_input(label="", placeholder='Enter a new todo')

