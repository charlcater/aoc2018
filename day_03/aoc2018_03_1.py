# Advent of Code 2018
# Day 03: No Matter How You Slice It -- Part 1

import numpy as np
import pandas as pd

sheet = np.zeros((1000, 1000))

with open('input.txt', 'r') as f:
    data = pd.read_csv('input.txt', delimiter=" ", header=None)

    for index, line in enumerate(f, start=1):
        id = int(data.iat[index - 1, 0].strip('#'))

        startpos = ((data.iat[index - 1, 2]).strip(':')).split(',')
        x = int(startpos[0])
        y = int(startpos[1])
        # print(x, y)

        size = (data.iat[index - 1, 3]).split('x')
        sizex = int(size[0])
        sizey = int(size[1])
        # print(sizex, sizey)

        claim = np.ones((sizex, sizey))
        # print('#{} Claim size: {}'.format(id, claim.shape))

        sheet[x:x + sizex, y:y + sizey] += claim

overlaps = np.count_nonzero(sheet > 1)  # find all nonzero elements > 1
print('Number of overlapping squares: {}'.format(overlaps))
