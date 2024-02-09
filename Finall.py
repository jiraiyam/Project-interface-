import streamlit as st

# Define login credentials
valid_username = "0"
valid_password = "0"

# Custom CSS styles with animations
custom_css = """
<style>
body {
    background-color: #f0f2f6;
    font-family: Arial, sans-serif;
}

.title {
    text-align: center;
    font-size: 24px;
    color: #333333;
}

.sidebar .sidebar-content {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
}

.sidebar .sidebar-content .stTextInput > div > div > div > input {
    border-radius: 5px;
    border: 1px solid #ccc;
    padding: 8px;
    width: 100%;
}

.login-button button {
    border-radius: 5px;
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    width: 100%;
    transition: background-color 0.3s ease;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}

.login-button button:hover {
    background-color: #0056b3;
}

.sidebar .sidebar-content .error-message {
    color: red;
}

.link-buttons-container {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}

.link-button {
    padding: 10px 20px;
    background-color: #222222;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.link-button:hover {
    background-color: #333333;
    box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.3);
}
</style>
"""


def main():
    # Inject custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Main title
    st.title("Education System ")
    st.markdown("---")

    # Sidebar login section
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    error_message = ""

    login_button = st.sidebar.button("Login", key="login_button", help="Click to log in")
    if login_button:
        if username == valid_username and password == valid_password:
            st.sidebar.success("Logged in as {}".format(username))
        else:
            error_message = "Invalid credentials"

    if error_message:
        st.sidebar.markdown(f'<p class="error-message">{error_message}</p>', unsafe_allow_html=True)

    # Links section
    st.markdown("<h3 class='title'>Parmajha System</h3>", unsafe_allow_html=True)
    with st.container():
        st.markdown(
            """
            <div class="link-buttons-container">
                <a href='https://chatbot-tsvhta2gvnqxznr3ovg8u8.streamlit.app/' class='link-button'>ParmaJhaBot</a>
                <a href='https://pdf2py-tkercuxngpkykbsuszfja6.streamlit.app/' class='link-button'>ParmaJha Chat pdf</a>
            </div>
            """,
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    main()
