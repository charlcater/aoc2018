# Advent of Code 2018
# Day 01: Chronal Calibration -- Part 1

with open('input.txt', 'r') as f:

    sum = 0

    lst = [int(i) for i in f.read().splitlines()]
    # lst = [+1, +2, +3]
    for i in lst:
        sum += i

    print('Final Total = {}'.format(sum))