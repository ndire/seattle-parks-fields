from datetime import time
from typing import Iterator, Optional

from constants import HOLIDAYS
from fields import Field
from time_block import TimeBlock

def clip_block_time_range(block: TimeBlock, start: time, end: time) -> Optional[TimeBlock]:
    if block.end <= start or block.start >= end:
        return None

    block.start = max(start, block.start)
    block.end = min(end, block.end)
    
    return block

def filter_duration(blocks: Iterator[TimeBlock], hours: float) -> Iterator[TimeBlock]:
    return filter(lambda b: b.duration_hours() > hours, blocks)

def clip_range_date(block: TimeBlock) -> Optional[TimeBlock]:
    if block.date in HOLIDAYS:
        return None
    elif block.date.weekday() < 5:
        # 5-10pm
        # TODO: move times to config, handle sunset
        end = time(hour=22) if block.field.lighted else time(hour=21)
        return clip_block_time_range(block, time(hour=17), end)
    else:
        # 9-8pm
        return clip_block_time_range(block, time(hour=9), time(hour=20))

def fields_with_turf(fields: Iterator[Field]) -> Iterator[Field]:
    return filter(lambda f: f.turf, fields)

def fields_with_bases(fields: Iterator[Field], base_length: int) -> Iterator[Field]:
    return filter(lambda f: base_length in f.bases, fields)