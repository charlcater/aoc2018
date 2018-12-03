# Advent of Code 2018
# Day 02: Inventory Management System -- Part 2

import difflib

with open('input.txt', 'r') as f:

	lst = [i for i in f.read().splitlines()]
	#lst = ['abcd', 'abce']
	length = len(lst)
	print('Total Lines: {}'.format(length))

	commonSet = list()

	for line in range(length):
		d = (difflib.get_close_matches(lst[line], lst, n=2, cutoff=0.96))
		
		for match in d:
			if match != lst[line]:
				#print(match)
				commonSet.append(match)
			else:
				continue

	print(commonSet)

ans = []
for x in commonSet:
	for y in commonSet:
		if len(ans) == 0:
			for i in range(len(x)):
				if x != y:
					if x[i] == y[i]:
						ans.append(x[i])
			print(''.join(ans))