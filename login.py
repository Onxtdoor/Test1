import streamlit as st

# Hardcoded username and password
USERNAME = "admin"
PASSWORD = "password123"

def login():
    st.title("Login Screen")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid username or password")

def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login()
    else:
        st.title("")
        st.markdown("<h1 style='text-align: center;'>Welcome to the site</h1>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()