# Advent of Code 2018
# Day 5: Alchemical Reduction -- Part 1

with open('input.txt', 'r') as f:

    # first strip the whitespace!
    polymer = list([i for i in f.read().splitlines()][0].strip())
    length = len(polymer)
    print('original length {}'.format(length))

    i = 0
    removed = 0

    while i < len(polymer)-1:
        if polymer[i].lower() == polymer[i+1].lower():
            if polymer[i].isupper() != polymer[i+1].isupper():
                # print('removing {}:{}'.format(i, polymer[i]))
                polymer.pop(i)
                # print('removing {}:{}'.format(i, polymer[i]))
                polymer.pop(i)
                removed += 2
                i = 0
            else:
                i += 1
        else:
            i += 1

    nlength = length - removed
    print(nlength)

    newpoly = str()

    for p in polymer:
        newpoly += p

with open('outpoly.txt', 'w') as o:
    print('{}'.format(newpoly), file=o)
