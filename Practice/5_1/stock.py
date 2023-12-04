# stock.py

import csv
from decimal import Decimal

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({repr(self.name)}, {repr(self.shares)}, {repr(self.price)})"

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
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