import sqlite3
import pandas as pd
from typing import List, Optional
from models import SymptomEntry
from datetime import datetime

class SymptomDatabase:
    def __init__(self, db_path: str = 'symptoms.db'):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS symptoms (
                    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,  -- CHANGED TO TEXT
                    symptom TEXT NOT NULL,
                    severity INTEGER NOT NULL CHECK (severity >= 1 AND severity <= 10),
                    duration_minutes INTEGER NOT NULL CHECK (duration_minutes > 0),
                    triggers TEXT,
                    notes TEXT
                )
            ''')
            conn.commit()
    
    def add_symptom(self, entry: SymptomEntry) -> bool:
        try:
            with sqlite3.connect(self.db_path) as conn:
                c = conn.cursor()
                # 🔥 USE entry.to_dict() - already string formatted
                data = entry.to_dict()
                c.execute('''
                    INSERT INTO symptoms (timestamp, symptom, severity, duration_minutes, triggers, notes)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    data['timestamp'],    # Already string '%Y-%m-%d %H:%M:%S'
                    data['symptom'],
                    data['severity'],
                    data['duration_minutes'],
                    data['triggers'],
                    data['notes']
                ))
                conn.commit()
            return True
        except Exception as e:
            print(f"Database error: {e}")
            return False
    
    def get_all_symptoms(self) -> pd.DataFrame:
        try:
            with sqlite3.connect(self.db_path) as conn:
                df = pd.read_sql_query("SELECT * FROM symptoms ORDER BY timestamp DESC", conn)
                if not df.empty:
                    df['timestamp'] = pd.to_datetime(df['timestamp'])
                return df
        except:
            return pd.DataFrame()
    
    def get_symptoms_by_date(self, date_str: str) -> pd.DataFrame:
        try:
            with sqlite3.connect(self.db_path) as conn:
                df = pd.read_sql_query(
                    "SELECT * FROM symptoms WHERE date(timestamp) = ? ORDER BY timestamp",
                    conn, params=(date_str,)
                )
                if not df.empty:
                    df['timestamp'] = pd.to_datetime(df['timestamp'])
                return df
        except:
            return pd.DataFrame()
    
    def delete_entry(self, entry_id: int) -> bool:
        try:
            with sqlite3.connect(self.db_path) as conn:
                c = conn.cursor()
                c.execute("DELETE FROM symptoms WHERE entry_id = ?", (entry_id,))
                conn.commit()
            return True
        except:
            return False
