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
    records = dict()
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

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    #rows = read_rides_as_tuples('../../Data/ctabus.csv')
    rows = read_rides_as_dict('../../Data/ctabus.csv')
    #rows = read_rides_as_class('../../Data/ctabus.csv')
    #rows = read_rides_as_namedtuples('../../Data/ctabus.csv')
    #rows = read_rides_as_slot('../../Data/ctabus.csv')
    print('Memory Use: Current %d Peak %d' % tracemalloc.get_traced_memory())