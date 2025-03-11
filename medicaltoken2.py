import streamlit as st
from datetime import datetime
import pandas as pd
import os

# Set page config and title with PCH logo
st.set_page_config(
    page_title="PCH - Token System",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
    <style>
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(5deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .stButton>button {
        background: linear-gradient(45deg, #2ecc71, #27ae60, #2ecc71);
        background-size: 200% 200%;
        animation: gradientBG 3s ease infinite;
        color: white;
        font-weight: bold;
        border-radius: 20px;
        padding: 1rem 2.5rem;
        border: none;
        box-shadow: 0 8px 20px rgba(46, 204, 113, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .stButton>button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 15px 30px rgba(46, 204, 113, 0.4);
    }
    .stTextInput>div>div>input {
        background-color: rgba(240, 248, 255, 0.8);
        border-radius: 15px;
        border: 2px solid #2ecc71;
        padding: 15px;
        transition: all 0.4s ease;
        backdrop-filter: blur(5px);
    }
    .stTextInput>div>div>input:focus {
        border-color: #27ae60;
        box-shadow: 0 0 20px rgba(46, 204, 113, 0.3);
        transform: scale(1.02);
    }
    .hospital-logo {
        text-align: center;
        margin-bottom: 20px;
        font-size: 3em;
        color: #2ecc71;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        animation: float 4s ease-in-out infinite;
    }
    .hospital-logo span {
        color: #3498db;
    }
    .hospital-logo .charitable {
        color: #27ae60;
    }
    .hospital-logo .hospital {
        color: #e74c3c;
    }
    .token-display {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
        margin: 30px 0;
        border: 3px solid rgba(46, 204, 113, 0.3);
        animation: pulse 2s infinite;
        backdrop-filter: blur(10px);
    }
    .success-message {
        background: linear-gradient(135deg, #e8fdf5 0%, #d4f7e6 100%);
        border-radius: 20px;
        padding: 30px;
        border-left: 8px solid #2ecc71;
        box-shadow: 0 10px 25px rgba(46, 204, 113, 0.2);
        transition: transform 0.3s ease;
    }
    .success-message:hover {
        transform: translateY(-5px);
    }
    .signature-line {
        border-top: 3px solid #2ecc71;
        width: 250px;
        margin: 25px 0 15px auto;
        box-shadow: 0 5px 15px rgba(46, 204, 113, 0.2);
    }
    .signature-text {
        text-align: right;
        margin-right: 25px;
        font-family: 'Cursive', cursive;
        color: #2ecc71;
    }
    .created-by {
        text-align: right;
        margin-top: 25px;
        font-style: italic;
        color: #555;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .stNumberInput>div>div>input {
        background-color: rgba(240, 248, 255, 0.8);
        border-radius: 15px;
        border: 2px solid #2ecc71;
        padding: 15px;
        transition: all 0.4s ease;
    }
    .stDataFrame {
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize token number and load existing data if available
if 'token_number' not in st.session_state:
    st.session_state.token_number = 1

# Load existing data from CSV if it exists
DATA_FILE = 'patient_records.csv'
if os.path.exists(DATA_FILE):
    patient_data = pd.read_csv(DATA_FILE)
    patient_data['Date'] = pd.to_datetime(patient_data['Date'])
else:
    patient_data = pd.DataFrame(columns=['Date', 'Token', 'Doctor', 'Patient', 'Age', 'Time', 'Fee'])

# Create tabs
tab1, tab2, tab3 = st.tabs(["✨ Input Form", "🎫 Token Display", "📊 Patient History"])

with tab1:
    # Custom PCH Logo with emojis
    st.markdown("""
        <div class='hospital-logo'>
            🏥 <span>P</span>EOPLES 👨‍⚕️<br>
            <span class='charitable'>CHARITABLE</span> ❤️<br>
            <span class='hospital'>HOSPITAL</span> 🏥
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center; color: #2ecc71; margin-bottom: 40px; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);'>PCH Token System</h1>", unsafe_allow_html=True)

    # Display contact info and address in a card
    st.markdown("""
        <div style='background: linear-gradient(135deg, white, #f8f9fa); padding: 30px; border-radius: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 3px solid rgba(46, 204, 113, 0.2);'>
            <h4 style='color: #2ecc71; font-size: 1.5em;'>📞 Contact Information</h4>
            <p style='font-size: 1.2em;'><strong>Phone:</strong> 03337095390</p>
            <p style='font-size: 1.2em;'><strong>Address:</strong> City Darya Khan Mari</p>
            <p style='color: #2ecc71; font-size: 1.4em; margin-top: 15px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'><strong>Consultation Fee: Rs. 50</strong></p>
        </div>
    """, unsafe_allow_html=True)

    # Rest of the code remains the same...
    current_date = datetime.now().strftime("%B %d, %Y")
    st.markdown(f"<div style='text-align: center; margin: 30px 0;'><h3 style='color: #2ecc71; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>📅 {current_date}</h3></div>", unsafe_allow_html=True)

    st.markdown(f"""
        <div class='token-display'>
            <h2 style='text-align: center; color: #4CAF50;'>Current Token Number: {st.session_state.token_number}</h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        doctor_name = st.text_input("👨‍⚕️ Doctor Name")
        patient_age = st.number_input("🎂 Patient Age", min_value=0, max_value=120)
    with col2:
        patient_name = st.text_input("👤 Patient Name")

    if st.button("Generate Next Token ➡️"):
        if patient_name and patient_age and doctor_name:
            current_time = datetime.now().strftime("%I:%M %p")
            
            new_data = {
                'Date': pd.Timestamp.now(),
                'Token': st.session_state.token_number,
                'Doctor': doctor_name,
                'Patient': patient_name,
                'Age': patient_age,
                'Time': current_time,
                'Fee': 50
            }
            
            patient_data = pd.concat([patient_data, pd.DataFrame([new_data])], ignore_index=True)
            
            patient_data = patient_data[
                patient_data['Date'] >= pd.Timestamp.now() - pd.Timedelta(days=8)
            ]
            
            patient_data.to_csv(DATA_FILE, index=False)
            
            st.session_state.token_number += 1
            
            st.query_params["tab"] = "Token Display"
            st.rerun()
        else:
            st.error("⚠️ Please fill in all details (Doctor Name, Patient Name, and Age)")

with tab2:
    if patient_data.empty:
        st.info("No tokens generated yet")
    else:
        latest_token = patient_data.iloc[-1]
        st.markdown(f"""
        <div class='success-message' style='text-align: center; font-size: 24px;'>
            <div class='hospital-logo'>
                🏥 <span>P</span>CH 👨‍⚕️<br>
            </div>
            <hr style='border-top: 3px solid #4CAF50;'>
            <p style='font-size: 48px; color: #4CAF50;'><strong>Token Number: {latest_token['Token']}</strong></p>
            <p style='font-size: 36px;'><strong>👨‍⚕️ Doctor:</strong> {latest_token['Doctor']}</p>
            <p style='font-size: 36px;'><strong>👤 Patient:</strong> {latest_token['Patient']}</p>
            <p style='font-size: 36px;'><strong>🎂 Age:</strong> {latest_token['Age']}</p>
            <p style='font-size: 36px;'><strong>⏰ Time:</strong> {latest_token['Time']}</p>
            <p style='font-size: 36px;'><strong>💰 Fee:</strong> Rs. 50</p>
            <div class='signature-line'></div>
            <div class='signature-text'>Dr. Signature</div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    if not patient_data.empty:
        st.markdown("""
            <div style='margin-top: 30px;'>
                <h3 style='color: #4CAF50;'>📋 Patient History (Last 8 Days)</h3>
            </div>
        """, unsafe_allow_html=True)
        display_df = patient_data.copy()
        display_df['Date'] = display_df['Date'].dt.strftime('%B %d, %Y')
        st.dataframe(display_df, use_container_width=True)
    else:
        st.info("No patient history available")

if st.button("🔄 Reset Token Numbers"):
    st.session_state.token_number = 1
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    st.success("🎉 Token numbers have been reset to 1")
    st.rerun()

if not patient_data.empty:
    csv = patient_data.to_csv(index=False)
    st.download_button(
        label="📥 Download Patient Records",
        data=csv,
        file_name='patient_records.csv',
        mime='text/csv',
    )

st.markdown("<hr style='margin: 30px 0;'>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 15px;'>
        <p style='color: #4CAF50;'>This automated token system helps manage patient queue efficiently.</p>
        <p style='color: #666; margin-top: 10px;'>Created with ❤️ by Dilsher Khaskheli</p>
    </div>
""", unsafe_allow_html=True)
