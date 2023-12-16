# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

Stock.create_init()