# redear.py
import csv
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
        dicts.append({ name:intern(func(val)) for name, func, val in zip(headers, types, row) })
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

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_csv_as_columns('../../Data/ctabus.csv', types=[str, str, str, int])
    print('Memory Use: Current %d Peak %d' % tracemalloc.get_traced_memory())