import streamlit as st
from datetime import datetime

# Set page config and title
st.set_page_config(page_title="PCH - Token System", page_icon="🏥")

# Custom CSS styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        background-color: #f0f8ff;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize token number in session state if not exists
if 'token_number' not in st.session_state:
    st.session_state.token_number = 1

# Title and description
st.title("🏥 PCH Token system")

# Display contact info and address
st.markdown("**Contact:** 03337095390")
st.markdown("**Address:** City Darya Khan Mari")
st.markdown("<h3 style='color: #4CAF50;'>Consultation Fee: Rs. 50</h3>", unsafe_allow_html=True)

# Display current date
current_date = datetime.now().strftime("%B %d, %Y")
st.write(f"Date: {current_date}")

# Display current token number
st.header(f"Current Token Number: {st.session_state.token_number}")

# Doctor and Patient information
doctor_name = st.text_input("Doctor Name")
patient_name = st.text_input("Patient Name")
patient_age = st.number_input("Patient Age", min_value=0, max_value=120)

# Generate new token
if st.button("Generate Next Token"):
    if patient_name and patient_age and doctor_name:
        # Display current patient details
        st.success(f"""
        Token Number: {st.session_state.token_number}

        Doctor Name: {doctor_name}

        Patient Name: {patient_name}

        Patient Age: {patient_age}

        Time: {datetime.now().strftime("%I:%M %p")}

        Fee: Rs. 50
        """)
        
        # Increment token number for next patient
        st.session_state.token_number += 1
        
        # Clear form after submission
        st.experimental_rerun()
    else:
        st.error("Please fill in all details (Doctor Name, Patient Name, and Age)")

# Reset token numbers
if st.button("Reset Token Numbers"):
    st.session_state.token_number = 1
    st.success("Token numbers have been reset to 1")
    st.experimental_rerun()

# Footer
st.markdown("---")
st.info("This automated token system helps manage patient queue efficiently.")
st.markdown("<div style='text-align: center; color: #666;'><small>Created by Dilsher Khaskheli</small></div>", unsafe_allow_html=True)
