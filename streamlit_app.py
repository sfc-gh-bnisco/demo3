import streamlit as st

st.title("Todo App")

# Initialize todo list with sample data
if "todos" not in st.session_state:
    st.session_state.todos = [
        {"task": "Buy groceries", "done": False},
        {"task": "Read a book", "done": True},
        {"task": "Go for a walk", "done": False},
        {"task": "Write weekly report", "done": False},
        {"task": "Call the dentist", "done": True},
    ]

# Add new todo
new_todo = st.text_input("Add a new todo", placeholder="What needs to be done?")
if st.button("Add") and new_todo:
    st.session_state.todos.insert(0, {"task": new_todo, "done": False})
    st.rerun()

st.divider()

# Display todos
for i, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([0.9, 0.1])
    with col1:
        checked = st.checkbox(todo["task"], value=todo["done"], key=f"todo_{i}")
        st.session_state.todos[i]["done"] = checked
    with col2:
        if st.button("X", key=f"del_{i}"):
            st.session_state.todos.pop(i)
            st.rerun()

# Summary
st.divider()
total = len(st.session_state.todos)
done = sum(1 for t in st.session_state.todos if t["done"])
st.caption(f"{done}/{total} completed")
