def portfolio_cost(file_name):
    total_cost = 0.0
    with open(file_name, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += (nshares * price)
            except ValueError as e:
                print("Couldn't parse:", repr(line))
                print("Reason:", e)
    return total_cost 

#print(portfolio_cost('../../Data/portfolio3.dat'))