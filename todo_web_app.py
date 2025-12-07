import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
        todo = st.session_state['new_todo']+"\n"
        todos.append(todo)
        functions.write_todos(todos)

st.title("My todo App")
st.subheader("This is my todo app")
st.write("This is for productivity.")

for index, items in enumerate(todos):
    checkbox = st.checkbox(items, key=items)
    if checkbox:
        todos.remove(todos[index])
        functions.write_todos(todos)
        del st.session_state[items]
        st.rerun()


st.text_input(label="",placeholder="Add new todo",
              on_change= add_todo, key='new_todo')