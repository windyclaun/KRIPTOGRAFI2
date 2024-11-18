import connect as conn
import streamlit as st
import hashlib

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        query = conn.run_query("SELECT * FROM users WHERE username = %s", (username))
        if query is not None and not query.empty:
            stored_password = query.iloc[0]['password']
            checkPass =  hashlib.sha256(password.encode()).hexdigest()
            if checkPass == stored_password:
                st.session_state['sudah_login'] = True
                st.session_state['username'] = username
                st.success("Login successful.")
                st.rerun()
            else:
                st.error("Invalid username or password.")
        else:
            st.error("Invalid username or password.")