import re
import streamlit as st


# def check_password(password):
#     score = 0

#     # check character

#     if len(password) > 8:
#         score += 1
#     else:
#         print("❌ password contain atlest 8 character")

#     # check letter

#     if re.search(r"[A-Z]" , password) and re.search(r"[a-z]" , password):
#         score += 1
#     else:
#         print("❌ password contain atlest one upper or lower case letter (a - z | A - Z)")

#     #check special character

#     if re.search(r"[!#$@%^&*]" , password):
#         score += 1
#     else:
#         print("❌ password contain atleast one special character (!#$@%^&*)")

#     #check digit

#     if re.search(r"\d" , password):
#         score += 1
#     else:
#         print("❌ add atleat one number (0-9)") 

#     if score == 4:
#         print("✅ strong password")
#     elif score == 3:
#         print("⚠️ Moderate Password - Consider adding more security features.")
#     else:
#         print(" ❌❌❌ weak password")

# password = input("Enter Password")
# check_password(password)


st.set_page_config(page_title="password strenght checker lock", page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.subheader("How Secure is Your Password? 🚀")
st.write("Shield your digital world with a rock-solid password. The stronger it is, the safer you stay! 🔒✨")

def password_strength_checker(password):
    score = 0
    feedback = []
  
  #check strenght

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must contain at least 8 characters.")
 
  #check letter

    if re.search(r"[A-z]" , password) and re.search(r"[a-z]" , password):
        score += 1
    else:
        feedback.append("❌ Include at least one uppercase and lowercase letter (A-Z , a-z).")

 #check digit 

    if re.search(r"\d" , password):
        score += 1
    else:
        feedback.append("❌ Include at least one number (0-9).")

#check special character

    if re.search(r"[!@#$%^&*]" , password):
        score += 1
    else:
        feedback.append("❌ Add at least one spcial character (!@#$%^&*).")


    if score == 4:
        st.success("✅ Strong Password! Your Account is well protected.")
    elif score == 3:
        st.warning("⚠️ Moderate password! Consider adding more security features")
    else:
        st.error("❌ Weak Password! Improve it for better security")

    if feedback:
        st.markdown("suggestion for improve your password 🔑")
        for tips in feedback:
            st.write(f"- {tips}")


password = st.text_input("Enter Your Password" , type="password")

if(password):
    password_strength_checker(password)
else:
    st.write("Please Enter Your Password To Check Its Security!!")