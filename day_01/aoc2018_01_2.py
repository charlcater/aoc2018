# Advent of Code 2018
# Day 01: Day 1: Chronal Calibration -- Part 2

def checkdupes(aList):
    global sum
    global i
    global dupefinder
    for j in aList:
        sum += j
        freqs.append(sum)
        if freqs.count(sum) > 1:
            print('Duplicate Frequency {} found on iteration {}'.format(freqs[i], i+1))
            dupefinder = True
            break
        else:
            i += 1
            continue
    return

with open('input2.txt', 'r') as f:
    i = 0  # counter
    sum = 0
    dupefinder = False
    freqs = []  # list of computed frequencies

    lst = [int(i) for i in f.read().splitlines()]
    # test cases
    # lst = [+1, -2, +3, +1, +1, -2, +3, +8, +10, -11]
    # lst = [-1, +1]
    # lst = [+3, +3, +4, -2, -4]
    # lst = [-6, +3, +8, +5, -6]
    # lst = [+7, +7, -2, -7, -4]

    p = 0

    while dupefinder == False:
        checkdupes(lst)
        lst.extend(lst)
        p += 1

    if dupefinder == True:
        print(freqs)
        print('Dupes found. List extened {} times'.format(p) )