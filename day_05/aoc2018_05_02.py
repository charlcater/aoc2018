# Advent of Code 2018
# Day 5: Alchemical Reduction -- Part 2

from string import ascii_lowercase

with open('input.txt', 'r') as f:

    # first strip the whitespace!
    polystr = [i for i in f.read().splitlines()][0].strip()
    # print('original length {}'.format(length))

    redstr = None

    finals = []

    for a in ascii_lowercase:
        print('Processing {}...'.format(a))
        redstr = polystr.replace(a , '')
        a = a.upper()
        redstr = redstr.replace(a , '')
        
        polymer = list(redstr)
        length = len(polymer)
        removed = 0
        i = 0
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
        finals.append(nlength)

print(finals)
print(min(finals))
