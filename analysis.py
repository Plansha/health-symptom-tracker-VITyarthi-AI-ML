import pandas as pd
from collections import Counter
from typing import Dict, List

class SymptomAnalyzer:
    @staticmethod
    def analyze_overview(df: pd.DataFrame) -> Dict:
        if df.empty:
            return {}
        
        return {
            'total_entries': len(df),
            'avg_severity': round(df['severity'].mean(), 1),
            'most_common_symptom': df['symptom'].mode()[0] if not df['symptom'].mode().empty else '',
            'total_duration_hours': round(df['duration_minutes'].sum() / 60, 1)
        }
    
    @staticmethod
    def get_symptom_stats(df: pd.DataFrame) -> pd.DataFrame:
        if df.empty:
            return pd.DataFrame()
        return df.groupby('symptom')['severity'].agg(['mean', 'count']).round(1)
    
    @staticmethod
    def get_trigger_insights(df: pd.DataFrame) -> Dict:
        triggers = []
        for triggers_str in df[df['triggers'] != '']['triggers']:
            triggers.extend([t.strip() for t in triggers_str.split(',')])
        return dict(Counter(triggers).most_common(10))
