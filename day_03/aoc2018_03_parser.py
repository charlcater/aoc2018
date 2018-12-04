# Advent of Code 2018
# Day 03: No Matter How You Slice It -- Part 1 & 2

# Using 'parse' is easier than creating the pandas dataframe, and could be useful for future problems

import numpy as np
import parse

claim_matcher = '''#{id:d} @ {x:d},{y:d}: {width:d}x{height:d}\n'''
fabric = np.zeros((1000, 1000), dtype=np.int)

# part 1

for line in open('input.txt'):
    r = parse.parse(claim_matcher, line)
    claim = fabric[r['y']: r['y'] + r['height'], r['x']: r['x'] + r['width']]
    claim[:] = claim + 1

print(np.sum(np.where(fabric > 1, 1, 0)))

# part 2

for line in open('input.txt'):
    r = parse.parse(claim_matcher, line)
    claim = fabric[r['y']: r['y'] + r['height'], r['x']: r['x'] + r['width']]

    if claim.max() == 1:
        print(r['id'])