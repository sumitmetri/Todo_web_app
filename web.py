"""
used streamlit platform to host the app
https url using streamlit cloud: https://sumitmetri-todo-web-app-web-214w2l.streamlit.app/
https url using Railway.app : https://web-production-89c7.up.railway.app/
"""

import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

    st.session_state["new_todo"] = ""   # session_state controls all the data in dictionary, use it along with the key to make changes

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
