from datetime import date

HOLIDAYS = (
    # Memorial Day
    [date(2025, 5, d) for d in [24, 25, 26]]
    +
    # 4th of July
    [date(2025, 7, d) for d in [3, 4, 5, 6]]
)
