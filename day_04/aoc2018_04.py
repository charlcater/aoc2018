# Advent of Code 2018
# Day 04: Repose Record -- Part 1
# Much much more elegant solution inspired mostyl by @jonathan_paulson
# https://www.reddit.com/r/adventofcode/comments/a2xef8/2018_day_4_solutions/eb1wb5a

from collections import defaultdict
lines = open('input.txt').read().split('\n')
lines.sort()


def parseTime(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])


C = defaultdict(int)  # counts total time asleep
CM = defaultdict(int)  # counts on which minutes asleep
guard = None
asleep = None
for line in lines:
    if line:
        time = parseTime(line)
        if 'begins shift' in line:
            guard = int(line.split()[3][1:])
            asleep = None
        elif 'falls asleep' in line:
            asleep = time
        elif 'wakes up' in line:
            for t in range(asleep, time):
                CM[(guard, t)] += 1
                C[guard] += 1


def bestguard(d):
    best = None
    for k, v in d.items():
        if best is None or v > d[best]:
            best = k
    return best


def bestmin(cm, g):
    m = ([k for k in cm.keys() if k[0] == g])
    mostm = None
    for k, v in m:
        if mostm is None or cm[(g, v)] > mostm:
            mostm = cm[(g, v)]
            best = v
    return best


best_guard = bestguard(C)
best_min = bestmin(CM, best_guard)
# print(best_guard, best_min)

most_guard, most_min = bestguard(CM)
# print(bestguard(CM))


print('Best guard: {}, Best minute: {}'.format(best_guard, best_min))
print('Best guard * best minute = {}'.format(best_guard * best_min))
print('')
print('Most guard: {}, Most minute: {}'.format(most_guard, most_min))
print('Most guard * most minute = {}'.format(most_guard * most_min))
