import streamlit as st
import re
st.set_page_config(page_title="Password strength checker")
st.title("PASSWORD STRENGTH CHECKER DESIGNED BY ONIZA FAZAL")

st.markdown("""
## Welcome to the ultimate password checker ##
 Here you can easily check your password strength i.e. whether your password 
is weak or strong and also you will get great tips for creating a strong password 
             """)



st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6f7ff; /* Light blue */

    }
    </style>
    """,
    unsafe_allow_html=True
)

password = st.text_input("Enter your password", type="password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score == 1
    else:
        feedback.append("Password should be atleast 8 characters long")
        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            score +=1
        else:
            feedback.append("Password should contain upperb and lower characters")

            if re.search(r'\d', password):
                score += 1
            else:
                feedback.append("Password should contain at least one digit")

                if re.search(r'[!#%%$@]', password):
                    score +=1
                    feedback.append("Password should containg at least one special character(!#$%%@).")

            if score == 4:
                    feedback.append("Your password is strong")
            elif score == 3:
                     feedback.append("Your password is medium strength. It could be stronger")

            else:
                feedback.append("Your password is week you need to create strong password")

            if feedback:
                 st.markdown("## Improvemnt suggestions")
            for tip in feedback:
                     st.write(tip)

            else: 
                 st.info("Please enter your passsword")
                



