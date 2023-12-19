# stock.py
from validate import *

class Stock():
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        self.shares -= nshares

    '''
    아래 코드가 작동하지 않는 이유 분석
    signature.bind 시에 첫번째 파라미터 self가 입력되지 않는다
    '''
    sell = ValidatedFunction(sell)
    
if __name__=='__main__':
    s = Stock('GOOG', 100, 490.1)
    s.sell(10)