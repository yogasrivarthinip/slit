import streamlit as st
import pandas as pd

st.title("Student Management System")

if "df" not in st.session_state:
    data = {
        "Name": [],
        "Age": []
    }
    st.session_state.df = pd.DataFrame(data)

df = st.session_state.df  

st.header("Add New Student")
with st.form("add_student_form", clear_on_submit=True):
    name = st.text_input("Student Name", key="add_name")
    age = st.number_input("Student Age", min_value=1, max_value=100, key="add_age")
    add_btn = st.form_submit_button("Add Student")
    
    if add_btn and name:
        new_row = pd.DataFrame({"Name": [name], "Age": [age]})
        st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
        st.success("Student added!")

st.header("View Students")
st.dataframe(df, use_container_width=True)

if st.button("Refresh List", key="refresh_list"):
    st.rerun()

st.header("Delete Student")
delete_name = st.text_input("Enter Student Name to Delete", key="delete_student")
if st.button("Delete", key="perform_delete"):
    if delete_name:
        before_len = len(df)
        st.session_state.df = df[df["Name"] != delete_name].reset_index(drop=True)
        if len(st.session_state.df) < before_len:
            st.success(f"Deleted '{delete_name}'!")
            st.dataframe(st.session_state.df)
        else:
            st.error("Student not found.")
    else:
        st.warning("Enter a name to delete.")