# redear.py
import csv
import tracemalloc
from sys import intern

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

def read_csv_as_dicts(filename, types):
    dicts = list()
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        dicts.append({ name:func(val) for name, func, val in zip(headers, types, row) })
    f.close()
    return dicts

def read_csv_as_columns(filename, types):
    d = DataCollection()
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        d.append(headers, types, row)
    f.close()
    return d

def read_csv_as_instances(filename, cls):
    records = []
    with open(filename, 'r') as f:
        rows  = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records

if __name__ == '__main__':
    tracemalloc.start()
    #rows = read_csv_as_dicts('../../Data/ctabus.csv', types=[intern, intern, str, int])
    rows = read_csv_as_columns('../../Data/ctabus.csv', types=[intern, intern, str, int])
    routeids = { id(row['route']) for row in rows }
    print(len(routeids))
    print('Memory Use: Current %d Peak %d' % tracemalloc.get_traced_memory())