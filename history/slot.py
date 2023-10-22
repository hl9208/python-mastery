class Stock:
    __slot__ = ('name', 'shares', 'price')
    # Great reduces the memory usage
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

from dataclasses import dataclass

@dataclass
class Stock2:
    name : str
    shares : int
    price : float

import typing

class Stock3(typing.NamedTuple):
    name : str
    shares : int
    price : float

from collections import namedtuple

Stock = namedtuple(Stock, ['name', 'shares', 'price'])