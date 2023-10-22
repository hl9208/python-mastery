file_path = "../../Data/portfolio.dat"

total_cost = 0.0

with open(file_path, 'r') as f:
    for line in f:
        fields = line.split()
        try:
            nshares = int(fields[1])
        except ValueError:
            print("Couldn't parse", line)
        price = float(fields[2])
        total_cost += (nshares * price)

print(f'{total_cost=}')
