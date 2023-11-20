# redear.py
import csv
import tracemalloc
from sys import intern
from abc import ABC, abstractmethod
from typing import Any

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records
    
    @abstractmethod
    def make_record(self, headers, row):
        pass

class DataCollection():
    def __init__(self):
        self.columns = []
    
    def __len__(self):
        return len(self.columns)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            NotImplemented
        elif isinstance(index, int):
            return self.columns[index]
        else:
            NotImplemented

    def append(self, headers, types, row):
        data = { name:func(val) for name, func, val in zip(headers, types, row) }
        self.columns.append(data)

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

def read_csv_as_dicts(filename, types):
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_columns(filename, types):
    d = DataCollection()
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        d.append(headers, types, row)
    f.close()
    return d

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls
    
    def make_record(self, headers, row):
        return self.cls.from_row(row)

def read_csv_as_instances(filename, cls):
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)

if __name__ == '__main__':
    tracemalloc.start()
    #rows = read_csv_as_dicts('../../Data/ctabus.csv', types=[intern, intern, str, int])
    rows = read_csv_as_columns('../../Data/ctabus.csv', types=[intern, intern, str, int])
    routeids = { id(row['route']) for row in rows }
    print(len(routeids))
    print('Memory Use: Current %d Peak %d' % tracemalloc.get_traced_memory())