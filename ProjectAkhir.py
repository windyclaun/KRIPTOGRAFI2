import streamlit as st
from daftar_halaman import Login, Register

if 'sudah_login' not in st.session_state:
    st.session_state['sudah_login'] = False

if st.session_state['sudah_login']:
    st.sidebar.title("Navigation")
    username = st.session_state['username']
    st.sidebar.success(f"Logged in as {username}")
    page = st.sidebar.radio("Go To", ["Dashboard", "Profile", "Settings"])
    # Dashboard.dashboard(page)
   
else:
    with st.sidebar:
        st.sidebar.title("Navigation")
        st.sidebar.warning("Not logged in")
        page = st.sidebar.radio("Select Page", ["Login", "Register"])
    if page == "Login":
        Login.login()
    elif page == "Register":
        Register.register()
