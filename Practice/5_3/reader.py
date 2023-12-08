# reader.py

import csv
from  typing import List

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    with open(filename) as file:
        records = csv_as_dicts(file, types)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of instances
    '''
    records = []
    with open(filename) as file:
        records = csv_as_instances(file, cls)
    return records

def csv_as_dicts(lines: List[str], types: List[function], headers: List[str]=None) -> List:
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: List[bytes], cls, headers: List[str]=None) -> List:
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records