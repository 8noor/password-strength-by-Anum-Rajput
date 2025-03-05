import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker By Anum Rajput", page_icon="🗝️", layout="centered")

#custom css
st.markdown("""
<style>
            .main {text-align: center;}
            .stTextInput {width: 60% !important; margin: auto;}
            .stButton {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
            .stButton button:hover {background-color: #45a049;}
            </style>
            """, unsafe_allow_html=True)

#page title and description
st.title("🔐Password Strength Generator")
st.write("Check the strength of your password and make it more secure.🔍")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    #check length
    if len(password) >= 8:
        score += 1 # increased score by 1
        feedback.append("❌ password should be **atleast 8 characters** long")

    #check for uppercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ password should contain **uppercase and lowercase letters**")

    #check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ password should contain ** at least one numbers (0-9)**.")

    #check for special characters
    if re.search(r"[!@#$%^&*()_+{}|:<>?~]", password):
        score += 1
    else:
        feedback.append("❌ Include ** at least one special character(!@#$%^&*)**.")

        #display password strength result
        if score == 0:
            st.error("❌ **Weak Password** - Please make it stronger.")
        elif score == 1:
            st.warning("⚠️ **Moderate password** - Consider improving  security by adding more features"   )
        elif score == 2:
            st.success("✅ **Strong Password** - Your password is strong and secure.")

        #display feedback
        if feedback:
            with st.expander(" 🔍**Improve your password**"):
                for item in feedback:
                    st.write(item)
                    password = st.text_input("Enter your password", type="password", help="Ensure your password is strong and secure 🔒.")

                #check button
                if st.button("Check Password Strength"):
                    if password:
                        check_password_strength(password)
                    else:
                        st.warning("⚠️ Please enter a password first!.") #show warning if password empty
        





