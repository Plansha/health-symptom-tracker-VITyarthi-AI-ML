import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
import pandas as pd
from database import SymptomDatabase
from utils import show_metrics
from analysis import SymptomAnalyzer

st.set_page_config(page_title="View Data", layout="wide")
st.header("📊 View All Data")

db = SymptomDatabase()
df = db.get_all_symptoms()

if not df.empty:
    stats = SymptomAnalyzer.analyze_overview(df)
    show_metrics(stats)
    
    st.dataframe(df, use_container_width=True)
    
    st.subheader("🗑️ Delete Entries")
    entry_id = st.number_input("Entry ID to delete", min_value=1, value=1)
    if st.button("Delete Entry"):
        if db.delete_entry(entry_id):
            st.success("Entry deleted!")
            st.rerun()
        else:
            st.error("Entry not found")
else:
    st.info("👆 Log some symptoms first!")
