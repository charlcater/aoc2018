# Advent of Code 2018
# Day 5: Alchemical Reduction -- Part 1
# Much much much faster soln, thanks to pixiethecat
# https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4e5kl

from string import ascii_lowercase

line = open("input.txt").read().splitlines()[0]

oldline = None
while oldline != line:
    oldline = line
    for a in ascii_lowercase:
        line = line.replace(a  + a.upper(),"")
        line = line.replace(a.upper()  + a,"")

print("Part1:")
print(len(line))

original = line
best = len(line)
for a in ascii_lowercase:
    line = original
    line = line.replace(a,"")
    line = line.replace(a.upper(),"")
    oldline = None
    while oldline != line:
        oldline = line
        for a in ascii_lowercase:
            line = line.replace(a  + a.upper(),"")
            line = line.replace(a.upper()  + a,"")

    best = len(line) if len(line) < best else best
print("Part2:")
print(best)