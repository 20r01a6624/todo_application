import streamlit as st
import functions

todos = functions.get_todos()

def add_sync():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)

st.title("My todo app")
st.write("this is an app ")

for index, todo in enumerate(todos):
    checkbox= st.checkbox(todo, key= "hello")
    if checkbox :
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
        



st.text_input(label="add:", placeholder= " add a new todo...",
              on_change= add_sync(), key= "new_todo")

print("hello")
st.session_state





