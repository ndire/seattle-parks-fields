import os.path
from datetime import time, date
import requests

from fields import FIELDS
from time_block import TimeBlock


BASE_URL = 'https://anc.apm.activecommunities.com/seattle/rest/reservation/resource/availability/daily'

def parse_block(field_key: str, day: str, desc: dict) -> TimeBlock:
    start = time.fromisoformat(desc['start_time'])
    end = time.fromisoformat(desc['end_time'])
    return TimeBlock(field_key, date.fromisoformat(day), start, end)

def get_availability(field_key, start_date, end_date) -> list[TimeBlock]:
    field_code = FIELDS[field_key]
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
    r = requests.get(os.path.join(BASE_URL, field_code), params=params)
    dates = r.json()['body']['details']['daily_details']
    return [parse_block(field_key, d['date'], desc) for d in dates for desc in d['times']] 