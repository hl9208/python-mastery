# A tuple
row = (route, date, daytype, rides)

# A dictionary
row = {
    'route': route,
    'date': date,
    'daytype': daytype,
    'rides': rides,
}

# A Class
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

#A named tuple
from collections import namedtuple
Row = namedtuple('Row', [route, date, daytype, rides])

# A class with __slots__
class Row:
    __slot__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides