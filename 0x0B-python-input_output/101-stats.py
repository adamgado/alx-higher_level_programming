#!/usr/bin/python3
"""read standard input and compute metrics"""
from sys import stdin

possible_codes = {'200': 0, '301': 0,
                  '400': 0, '401': 0,
                  '403': 0, '404': 0,
                  '405': 0, '500': 0}
size = i = 0


def print_metrics(size, status_codes):
    """print metrics"""
    print("File size: {}".format(size))
    for key, value in sorted(possible_codes.items()):
        print("{}: {}".format(key, value))


try:
    for a in stdin:
        seperated = a.split()
        if len(seperated) >= 2:
            code = seperated[-2]
            size += int(seperated[-1])
            if code in possible_codes:
                possible_codes[code] += 1
        i += 1
        if i % 10 == 0:
            print_metrics(size, possible_codes)
    print_metrics(size, possible_codes)
except KeyboardInterrupt as e:
    print_metrics(size, possible_codes)
