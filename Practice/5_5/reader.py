# reader.py

import csv
import logging
from  typing import List

logger = logging.getLogger(__name__)

def read_csv_as_dicts(filename, types, *, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    with open(filename) as file:
        records = csv_as_dicts(file, types)
    return records

def read_csv_as_instances(filename, cls, *, headers=None):
    '''
    Read CSV data into a list of instances
    '''
    records = []
    with open(filename) as file:
        records = csv_as_instances(file, cls, headers)
    return records

def csv_as_dicts(lines: List[str], types: List[str], *,  headers: List[str]=None) -> List:
    converter = lambda headers, row: { name: func(val) for name, func, val in zip (headers, types, row)}
    return convert_csv(lines, converter)

def csv_as_instances(lines: List[bytes], cls, *, headers: List[str]=None) -> List:
    converter = lambda headers, row: cls.from_row(row)
    return convert_csv(lines, converter)

def convert_csv(lines, func, *, headers=None):
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    # 에러 핸들링을 위해 다시 map에서 다시 for문 사용
    for idx, row in enumerate(rows):
        try:
            records.append(func(headers, row))
        except ValueError as e:
            logger.warn(f"WARNING:reader:Row {idx}: Bad row: {row}")
            logger.warn(f"DEBUG:reader:Row {idx}: Reason: {e}")
            continue
    return records