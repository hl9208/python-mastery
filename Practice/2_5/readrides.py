# readride.py

import csv
import collections.abc

def template(filename):
    '''
    read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # Skip header
        for row in rows:
            records.append(record)
    return records

def read_rides_as_tuples(filename):
    '''
    read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # Skip header
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dict(filename):
    '''
    read the bus ride data as a list of dictionarys
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # Skip header
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(record)
    return records

def read_rides_as_class(filename):
    '''
    read the bus ride data as a list of class instances
    '''
    class Row:
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # Skip header
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

def read_rides_as_namedtuples(filename):
    '''
    read the bus ride data as a list of namedtuples
    '''
    from collections import namedtuple
    Row = namedtuple('Row', ('route', 'date', 'daytype', 'rides'))
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # Skip header
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

def read_rides_as_slot(filename):
    '''
    read the bus ride data as a list of slot
    '''
    class Row:
        __slot__ = ['route', 'date', 'daytype', 'rides']
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # Skip header
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

def read_rides_as_columns(filename):
    '''
    Read the bus ride date into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(row[3])
    return dict(route=routes, dates=dates, daytypes=daytypes, numride=numrides)

class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []    # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        """
        인덱스를 받을 수 있게 한다.
        인덱스 객체를 그대로 출력해보면 들어오는 객체로 slice 혹은 int가 있다.
        slice object가 들어오면 slice.start, slice.stop, slice.step을 사용한다.
        """
        if isinstance(index, slice):
            r = RideData()
            for idx in range(index.start, index.stop, 1 if index.step == None else index.step):
                r.routes.append(self.routes[idx])
                r.dates.append(self.dates[idx])
                r.daytypes.append(self.daytypes[idx])
                r.numrides.append(self.numrides[idx])
                '''
                routes = []
                dates = []
                daytypes = []
                numrides = []
                start = index.start
                stop = index.stop
                step = 1 if index.step == None else index.step
                data = {
                    'routes': self.route[start:stop:step],
                    'dates': self.dates[start:stop:step],
                    'daytypes': self.daytypes[start:stop:step],
                    'numrides': self.numrides[start:stop:step]
                    }
                '''
            return r

        elif isinstance(index, int):
            return {
                'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]
            }
        else:
            NotImplemented

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    #rows = read_rides_as_tuples('../../Data/ctabus.csv')
    rows = read_rides_as_class('../../Data/ctabus.csv')
    #rows = read_rides_as_class('../../Data/ctabus.csv')
    #rows = read_rides_as_namedtuples('../../Data/ctabus.csv')
    #rows = read_rides_as_slot('../../Data/ctabus.csv')
    print('Memory Use: Current %d Peak %d' % tracemalloc.get_traced_memory())