import streamlit as st
import connect as conn


def register():
    st.title("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    re_password = st.text_input("Re-enter Password", type="password")
    if st.button("Register"):
        if not username or not password or not re_password:
            st.error("Username and password cannot be empty.")
            return
        if password != re_password:
            st.error("Passwords do not match.")
            return

        query = conn.run_query("SELECT * FROM users WHERE username = '" + username + "';", fetch=True)
        if query is not None and not query.empty:
            conn.run_query("INSERT INTO users (username, password) VALUES (%s, %s);", (username, password), fetch=False)
            st.success("Registration successful.")
            
        else:
            st.error("Username already exists.")
            return