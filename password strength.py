import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker By Anum Rajput", page_icon="🗝️", layout="centered")

# Custom CSS for button styling
st.markdown("""
    <style>
        .centered-button {
            display: flex;
            justify-content: center;
        }
        .styled-button {
            background-color: salmon;
            color: orchid;
            font-size: 18px;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
            text-align: center;
        }
        .styled-button:hover {
            background-color: lightcoral;
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

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters** long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain **uppercase and lowercase letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*()_+{}|:<>?~]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

    if score == 0:
        st.error("❌ **Weak Password** - Please make it stronger.")
    elif score == 1:
        st.warning("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    elif score >= 3:
        st.success("✅ **Strong Password** - Your password is strong and secure.")

    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your password", type="password", help="Ensure your password is strong and secure 🔒.")

st.markdown('<div class="centered-button"><button class="styled-button" onclick="document.getElementById(\'check\').click()">Check Password Strength</button></div>', unsafe_allow_html=True)

if st.button("Check Password Strength", key="check"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
