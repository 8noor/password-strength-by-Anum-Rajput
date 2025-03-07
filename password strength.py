import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker By Anum Rajput", page_icon="🗝️", layout="centered")

# Custom CSS
st.markdown("""
 <style>
        .main {
            text-align: center;
        }
        div[data-testid="stTextInput"] {
            width: 60% !important;  
            margin: auto;
        }
        .centered-button {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .stButton > button {
            width: 60%;
            background-color:silver;
            color: blue;
            font-size: 18px;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
            text-align: center;
        }
        .stButton > button:hover {
            background-color: pink;
        }
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Checker")
st.write("Check the strength of your password and make it more secure. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters** long.")

    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain **uppercase and lowercase letters**.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one number (0-9)**.")

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+{}|:<>?~]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

    # Display password strength result
    if score == 0:
        st.error("❌ **Weak Password** - Please make it stronger.")
    elif score == 1:
        st.warning("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    elif score >= 3:
        st.success("✅ **Strong Password** - Your password is strong and secure.")

    # Display feedback
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# User input
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong and secure 🔒.")

# Check button
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
