# reader.py

import csv
from  typing import List

def read_csv_as_dicts(filename, types, *, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    with open(filename) as file:
        records = csv_as_dicts(file, types, headers)
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
    # for문을 map으로 대체
    records = list(map(lambda row: func(headers, row), rows))
    return records