import os.path
from datetime import time, date
import requests

from fields import FIELD_MAP, Field
from time_block import TimeBlock


BASE_URL = 'https://anc.apm.activecommunities.com/seattle/rest/reservation/resource/availability/daily'

def parse_block(field: Field, day: str, desc: dict) -> TimeBlock:
    start = time.fromisoformat(desc['start_time'])
    end = time.fromisoformat(desc['end_time'])
    return TimeBlock(field, date.fromisoformat(day), start, end)

def get_availability(field: Field, start_date: str, end_date: str) -> list[TimeBlock]:
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'customer_id': 0,
        'company_id': 0,
        'event_type_id': -1,
        'attendee': 1,
        'no_cache': 'true',
        'locale': 'en-US'
    }
    r = requests.get(os.path.join(BASE_URL, field.id), params=params)
    dates = r.json()['body']['details']['daily_details']
    return [parse_block(field, d['date'], desc) for d in dates for desc in d['times']] 