# stock.py

import csv
from decimal import Decimal

class Stock:
    __slots__ = ('name', '_shares', '_price')
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected {self._types[1].__name__}')
        if value < 0:
            raise ValueError('Expected positive')
        self._shares = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'Expected {_types[2]}')
        if value < 0.0:
            raise ValueError('Expected positive')
        self._price = value

    def sell(self, nshares):
        self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = Stock.from_row(row)
            portfolio.append(record)
    return portfolio

def print_portfolio(portfolio):
    print("%10s %10s %10s" % ("name", "shares", "price"))
    print(('-'*10 + ' ')*3)
    for s in portfolio:
        print(f"{s.name:>10} {s.shares:>10d} {s.price:>10.2f}")

class DStock(Stock):
    types = (str, int, Decimal)

if __name__=="__main__":
    portfolio = read_portfolio('../../Data/portfolio.csv')
    print_portfolio(portfolio)