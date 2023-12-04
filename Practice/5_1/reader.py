# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                      for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of instances
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records

def csv_as_dicts(lines, types):
    records = []
    headers = next(lines)
    for line in lines:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, line.split()) }
        records.append(record)
    return records

def csv_as_instances(lines, cls):
    records = []
    headers = next(lines)
    for line in lines:
        record = cls.from_row(line)
        records.append(record)
    return records