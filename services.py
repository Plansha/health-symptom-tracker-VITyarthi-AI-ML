from models import SymptomEntry
from datetime import datetime
from typing import List

class SymptomService:
    @staticmethod
    def create_entry(symptom: str, severity: int, duration: int, 
                    triggers: List[str], notes: str, timestamp=None):
        return SymptomEntry(
            timestamp=timestamp or datetime.now(),
            symptom=symptom,
            severity=severity,
            duration_minutes=duration,
            triggers=triggers,
            notes=notes
        )
    
    @staticmethod
    def validate_entry(entry: SymptomEntry) -> bool:
        return (1 <= entry.severity <= 10 and 
                entry.duration_minutes > 0 and 
                entry.symptom.strip() != "")
