import streamlit as st
from daftar_halaman import Login, Register, Home

if 'sudah_login' not in st.session_state:
    st.session_state['sudah_login'] = False

if st.session_state['sudah_login']:
    st.sidebar.image("logo.png", use_container_width=True)
    st.sidebar.title("CatEyeProctor")
    st.sidebar.title("Menu")
    username = st.session_state['username']
    st.sidebar.success(f"Hai, {username}")
    page = st.sidebar.radio("Go To", ["Text", "Steganography", "File"])
    if st.sidebar.button("Logout"):
        st.session_state['sudah_login'] = False
        st.rerun()
    Home.menu(page) 
   
else:
    with st.sidebar:
        st.sidebar.image("logo.png", use_container_width=True)
        st.sidebar.title("CatEyeProctor")
        st.sidebar.warning("Not logged in")
        page = st.sidebar.radio("Select Page", ["Login", "Register"])
    if page == "Login":
        Login.login()
    elif page == "Register":
        Register.register()
