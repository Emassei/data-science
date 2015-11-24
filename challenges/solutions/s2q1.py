import csv  # this was the solution from Question1
import numpy

FIELDNAMES = ['', 'id', 'priceLabel', 'name', 'brandId', 'brandName',
              'imageLink', 'desc', 'vendor', 'patterned', 'material']

DATATYPES = [('myint', 'i'), ('myid', 'i'), ('price', 'f8'), ('name', 'a200'),
             ('brandId', '<i8'), ('brandName', 'a200'), ('imageUrl', '|S500'),
             ('description', '|S900'), ('vendor', '|S100'),
             ('pattern', '|S50'), ('material', '|S50'), ]


def open_with_csv(filename, d='\t'):
    data = []
    with open(filename) as tsvin:
        tsvin = csv.reader(tsvin, delimiter=d)
        for row in tsvin:
            data.append(row)
    return data

data_from_csv = open_with_csv('data.csv')


def load_data(filename, d='\t'):
    my_csv = numpy.genfromtxt(filename, delimiter=d, skip_header=1,
                              invalid_raise=False, names=FIELDNAMES,
                              dtype=DATATYPES)
    return my_csv

my_csv = load_data('data.csv')
