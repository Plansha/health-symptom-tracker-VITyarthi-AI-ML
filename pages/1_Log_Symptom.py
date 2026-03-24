import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# Fix imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SymptomDatabase
from services import SymptomService
from models import SymptomEntry

st.set_page_config(page_title="Log Symptom", layout="wide")
st.header("📝 Log New Symptom")

db = SymptomDatabase()

col1, col2 = st.columns(2)

with col1:
    symptom = st.selectbox("Symptom", 
                          ["headache", "fatigue", "nausea", "back pain", "stomach ache", 
                           "fever", "cough", "sore throat", "anxiety", "insomnia", "other"])
    severity = st.slider("Severity (1-10)", 1, 10, 5)

with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, value=60)
    
    date_input = st.date_input("Date", value=pd.Timestamp.now().date())
    time_input = st.time_input("Time", value=pd.Timestamp.now().time())
    timestamp = datetime.combine(date_input, time_input)  # 🔥 Python datetime

triggers = st.multiselect("Possible Triggers", 
                         ["stress", "poor sleep", "caffeine", "screen time", 
                          "diet", "weather", "exercise", "medication", "dehydration"])

notes = st.text_area("Additional Notes", height=100)

if st.button("💾 Save Symptom", type="primary"):
    try:
        entry = SymptomService.create_entry(symptom, severity, duration, triggers, notes, timestamp)
        
        if SymptomService.validate_entry(entry):
            if db.add_symptom(entry):
                st.success("✅ Symptom logged successfully!")
                st.balloons()
                st.experimental_rerun()  # 🔥 FIXED: Use experimental_rerun
            else:
                st.error("❌ Database save failed")
        else:
            st.error("❌ Invalid data")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
