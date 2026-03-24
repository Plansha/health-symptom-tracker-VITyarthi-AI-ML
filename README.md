# Health Symptom Tracker

A professional Streamlit web application for tracking health symptoms, analyzing patterns, and generating medical reports for BYOP submission.

## 🚀 Quick Start

```bash
pip install streamlit pandas plotly
streamlit run app.py
Open Local URL: http://localhost:8501. The app automatically creates symptoms.db.

✨ Features:
1. Log symptoms with severity (1-10), duration, and triggers
2. View all entries in interactive data table
3. Analyze patterns through charts and statistics
4. Export data as CSV for doctors
5. Multi-page navigation (Log/View/Analyze/Export)

Files
app.py (main)
database.py (SQLite)
models.py (data model)
services.py (logic)
pages/1_Log_Symptom.py
pages/2_View_Data.py
pages/3_Analysis.py
pages/4_Export.py

Tech
Streamlit | Pandas | Plotly | SQLite

## 📱 Demo Screenshots
![Homepage](screenshots/homepage.png)
![Log Symptom](screenshots/log-symptom.png)
![Charts](screenshots/charts.png)
![Export](screenshots/export.png)

