from datetime import datetime, timedelta
from typing import List


id2section = {
    '100': '정치',
    '101': '경제',
    '102': '사회',
    '103': '생활/문화',
    '104': '세계',
    '105': 'IT/과학'
}
section2id = {v: k for k, v in id2section.items()}


def get_datetimes(start: datetime, stop: datetime, step: timedelta=timedelta(days=1)) -> List[str]:
    dates = []
    x = start
    while x < stop:
        dates.append(x.strftime('%Y%m%d'))
        x += step
    return dates
