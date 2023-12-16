# teststock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_create_keyword(self):
        s = stock.Stock(name='GOOG', shares=100, price=490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = stock.Stock(name='GOOG', shares=100, price=490.1)
        self.assertEqual(s.cost(), 49010)

    def test_sell(self):
        s = stock.Stock(name='GOOG', shares=100, price=490.1)
        s.sell(50)
        self.assertEqual(s.shares, 50)

    def test_from_row(self):
        from_row = stock.Stock.from_row(["GOOG", '100', '490.1'])
        s = stock.Stock(name='GOOG', shares=100, price=490.1)
        self.assertEqual(from_row, s)

    def test_reqr(self):
        s = stock.Stock(name='GOOG', shares=100, price=490.1)
        repr = s.__repr__()
        text = "Stock('IBM', 50, 55)"
        self.assertEqual(repr, text)

    def test_eq(self):
        s1 = stock.Stock(name='GOOG', shares=100, price=490.1)
        s2 = stock.Stock(name='GOOG', shares=100, price=490.1)
        self.assertEqual(s1, s2)

    def test_shares_badtype(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '50'

    def test_shares_badvalue(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.shares = -50

    def test_price_badtype(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = '490.1'

    def test_price_badvalue(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.price = -490.1

    def test_bad_attribute(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = 100

if __name__ == '__main__':
    unittest.main()