from datetime import date, datetime, time
from dataclasses import dataclass

@dataclass
class TimeBlock:
    field_key: str
    date: date
    start: time
    end: time

    def _day_name(self, short=False) -> str:
        fmt = '%a' if short else '%A'
        return self.date.strftime(fmt)

    def __repr__(self):
        return (
            f"{self.field_key} {self._day_name(True)} {self.date}:" +
            f" {_time_fmt(self.start)}-{_time_fmt(self.end)}"
        )

    def duration_hours(self) -> float:
        return (_dt_from_time(self.end) - _dt_from_time(self.start)).total_seconds() / 3600

    def to_json(self):
        return {
            'Field': self.field_key,
            'Date': self.date,
            'Day' : self._day_name(),
            'Start': self.start,
            'End': self.end,
        }

def _time_fmt(t: time) -> str:
    return t.strftime('%I:%M%p')

def _dt_from_time(t: time) -> datetime:
    return datetime(2000, 1, 1, hour=t.hour, minute=t.minute)
