from s2q2 import *

# All of these calculate the sum of the all the row[2]


def calculate_sum(data_sample):
    # total uses 0 as a starting point
    total = 0
    # now we loop through the rows in the data sample
    # skipping row 1 with [1:];
    for row in data_sample[1:]:
        # next we foucus our loop on just the float 'numbers' in row[2]
        price = float(row[2])
        # from there we then add each float (row[2]) as a price
        # to create the total, this sums the numbers
        total += price
    return total

# print(calculate_sum(data_from_csv))


def calculate_sum_succinct(data_sample):
    # here we are doing the same thing
    prices = [float(row[2]) for row in data_sample[1:]]
    return sum(prices)

# print(calculate_sum_succinct(data_from_csv))


def calculate_sum_concise(data_sample):
    prices = list(map(lambda x: float(x[2]), data_sample[1:]))
    return sum(prices)

# print(calculate_sum_concise(data_from_csv))


def calculate_numpy_sum(price):
    prices_in_float = [float(line) for line in price]
    total = numpy.sum(prices_in_float)
    return(total)

price = my_csv['priceLabel']
# print(calculate_numpy_sum(price))
