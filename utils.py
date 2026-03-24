import streamlit as st

def show_metrics(stats: dict):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Entries", stats.get('total_entries', 0))
    with col2:
        st.metric("Avg Severity", stats.get('avg_severity', 0))
    with col3:
        st.metric("Most Common", stats.get('most_common_symptom', 'None'))
    with col4:
        st.metric("Total Hours", stats.get('total_duration_hours', 0))
