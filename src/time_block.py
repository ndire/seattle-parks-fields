from datetime import date, datetime, time
from dataclasses import dataclass

@dataclass
class TimeBlock:
    field_key: str
    date: date
    start: time
    end: time

    def __repr__(self):
        return f"{self.field_key} {self.date}: {self.start}-{self.end}"

    def duration_hours(self) -> float:
        return (_dt_from_time(self.end) - _dt_from_time(self.start)).total_seconds() / 3600

    def to_json(self):
        return {
            'Field': self.field_key,
            'Date': self.date,
            'Start': self.start,
            'End': self.end,
        }

def _dt_from_time(t):
    return datetime(2000, 1, 1, hour=t.hour, minute=t.minute)
