import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
import plotly.express as px
import pandas as pd
from database import SymptomDatabase
from analysis import SymptomAnalyzer
from utils import show_metrics

st.set_page_config(page_title="Analysis", layout="wide")
st.header("🔍 Detailed Analysis")

db = SymptomDatabase()
df = db.get_all_symptoms()

if not df.empty:
    stats = SymptomAnalyzer.analyze_overview(df)
    show_metrics(stats)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.line(df, x='timestamp', y='severity', color='symptom',
                      title="Severity Over Time")
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        symptom_stats = df['symptom'].value_counts()
        fig2 = px.bar(x=symptom_stats.index, y=symptom_stats.values,
                     title="Symptom Frequency")
        st.plotly_chart(fig2, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Severity by Symptom")
        severity_stats = SymptomAnalyzer.get_symptom_stats(df)
        st.dataframe(severity_stats)
    
    with col2:
        st.subheader("Top Triggers")
        triggers = SymptomAnalyzer.get_trigger_insights(df)
        if triggers:
            trigger_df = pd.DataFrame(list(triggers.items()), 
                                    columns=['Trigger', 'Count'])
            st.dataframe(trigger_df)
else:
    st.warning("📝 Log symptoms first for analysis!")
