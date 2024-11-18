import connect as conn
import streamlit as st

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        result = conn.run_query(query, (username, password))
        if result is not None and not result.empty:
            st.session_state['sudah_login'] = True
            st.session_state['username'] = username
            st.success("Login successful.")
        else:
            st.error("Invalid username or password.")