import streamlit as st
from database import SymptomDatabase
from analysis import SymptomAnalyzer
from utils import show_metrics

st.set_page_config(page_title="Health Symptom Tracker", layout="wide")
st.title("🏥 Health Symptom Tracker")
st.markdown("**Welcome! Use the sidebar to navigate between pages.**")

db = SymptomDatabase()
stats = SymptomAnalyzer.analyze_overview(db.get_all_symptoms())
show_metrics(stats)

st.info("👈 Click sidebar pages to log symptoms, view data, analyze patterns!")
