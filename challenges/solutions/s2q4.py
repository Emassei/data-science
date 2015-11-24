from s2q3 import *


def find_average(data_sample, header=False):
    if header:
        data_sample = data_sample[1:]
    total = calculate_sum(data_sample)
    size = number_of_records(data_sample)
    average = total / size
    return average

average_price = find_average(data_from_csv, True)
# print(average_price)

# this '{:03.2f}' mess is how you get two decimal places formatted
print('{:03.2f}'.format(average_price))

# good to use types to debug
print(type(average_price))

midpoint = int(round(number_of_ties / 2))

message = "Average of {} half = {}"

print(message.format("1st", find_average(data_from_csv[:midpoint], True)))
print(message.format("2nd", find_average(data_from_csv[midpoint:], False)))
