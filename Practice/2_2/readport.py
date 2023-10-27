# readport.py

import csv
import readrides
from collections import Counter

# A fuction that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2]),
            }
            portfolio.append(record)
    return portfolio

def four_question(filename):
    rows = readrides.read_rides_as_dict(filename)
    return rows

def number_of_bus_routes(rows):
    # How many bus routes exist in Chicago?
    number_of_route = {row['route'] for row in rows}

def rides_on_date(rows, number, date):
    # example of date: '02/22/0211'
    # How many people rode the number 22 bus on February 2, 2011?
    # What about any route on any date of your choosing?
    rides = sum([int(row['rides']) for row in rows
                 if row['date'] == date and row['route'] == str(number)])
    return rides

def each_rides_numbers(rows):
    # What is the total number of rides taken on each bus route?
    totals = Counter()
    for row in rows:
        totals[row['route']] += int(row['rides'])
    return totals

def greatest_routes(rows):
    # What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
    target_years = [str(year) for year in range(2001, 2012)]
    totals = Counter()
    for row in rows:
        if row['date'][-4:] in target_years:
            totals[row['route']] += int(row['rides'])
    return totals.most_common(5)