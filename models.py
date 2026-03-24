from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import pandas as pd

@dataclass
class SymptomEntry:
    entry_id: Optional[int] = None
    timestamp: datetime = None
    symptom: str = ""
    severity: int = 5
    duration_minutes: int = 60
    triggers: List[str] = None
    notes: str = ""
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
        if self.triggers is None:
            self.triggers = []
    
    def to_dict(self):
        """Convert to SQLite-compatible dictionary"""
        return {
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),  # 🔥 STRING for SQLite
            'symptom': self.symptom,
            'severity': self.severity,
            'duration_minutes': self.duration_minutes,
            'triggers': ','.join(self.triggers),
            'notes': self.notes
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create from database row"""
        entry = cls()
        entry.entry_id = data.get('entry_id')
        entry.timestamp = pd.to_datetime(data.get('timestamp'))
        entry.symptom = data.get('symptom', '')
        entry.severity = data.get('severity', 5)
        entry.duration_minutes = data.get('duration_minutes', 60)
        entry.notes = data.get('notes', '')
        entry.triggers = data.get('triggers', '').split(',') if data.get('triggers') else []
        return entry

    def __repr__(self):
        return f"SymptomEntry(id={self.entry_id}, symptom={self.symptom}, severity={self.severity})"
