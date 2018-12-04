# Advent of Code 2018
# Day 03: No Matter How You Slice It -- Part 1 & 2

import numpy as np
import pandas as pd

itercount = 0
itercount2 = 0

sheet = np.zeros((1000, 1000))

with open('input.txt', 'r') as f:
    data = pd.read_csv('input.txt', delimiter=" ", header=None)

# Part 1

    for index, line in enumerate(f):
        id = int(data.iat[index, 0].strip('#'))

        startpos = ((data.iat[index, 2]).strip(':')).split(',')
        x = int(startpos[0])
        y = int(startpos[1])
        # print(x, y)

        size = (data.iat[index, 3]).split('x')
        sizex = int(size[0])
        sizey = int(size[1])
        # print(sizex, sizey)

        claim = np.ones((sizex, sizey))
        # print('#{} Claim size: {}'.format(id, claim.shape))

        sheet[x:x + sizex, y:y + sizey] += claim

overlaps = np.count_nonzero(sheet > 1)  # find all nonzero elements > 1
print('Number of overlapping squares: {}'.format(overlaps))


#  Part 2 (run iteration again, because we need a fully populated sheet to analyse)

with open('input.txt', 'r') as f:

    for index, line in enumerate(f):
        id = int(data.iat[index, 0].strip('#'))

        startpos = ((data.iat[index, 2]).strip(':')).split(',')
        x = int(startpos[0])
        y = int(startpos[1])

        size = (data.iat[index, 3]).split('x')
        sizex = int(size[0])
        sizey = int(size[1])

        nsquares = sizex * sizey
        # print('Size: {}'.format(numsquares))

        region = sheet[x:x + sizex, y:y + sizey]

        if np.count_nonzero(region == 1) == nsquares:
            print('Non overlapping region found, ID {}'.format(id))
            break
