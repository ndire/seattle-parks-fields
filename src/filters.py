from datetime import time
from typing import Optional

from constants import HOLIDAYS
from time_block import TimeBlock

def clip_block_time_range(block, start, end) -> Optional[TimeBlock]:
    if block.end <= start or block.start >= end:
        return None

    block.start = max(start, block.start)
    block.end = min(end, block.end)
    
    return block

def filter_duration(blocks, hours):
    return list(filter(lambda b: b.duration_hours() > hours, blocks))

def clip_range_date(block: TimeBlock) -> Optional[TimeBlock]:
    if block.date in HOLIDAYS:
        return None
    elif block.date.weekday() < 5:
        # 5-10pm
        return clip_block_time_range(block, time(hour=17), time(hour=21))
    else:
        # 9-8pm
        return clip_block_time_range(block, time(hour=9), time(hour=20))