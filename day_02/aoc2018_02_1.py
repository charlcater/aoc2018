# Advent of Code 2018
# Day 02: Inventory Management System -- Part 1

with open('input.txt', 'r') as f:

	doubles = 0
	triples = 0
	line = 0

	lst = [i for i in f.read().splitlines()]

	for scanned in lst:
		doublepass = False
		triplepass = False
		for letter in scanned:
			if scanned.count(letter) == 2:
				while doublepass == False:
					doubles += 1
					# print('double in line {}'.format(line))
					doublepass = True
				
			elif scanned.count(letter) == 3:
				while triplepass == False:
					triples += 1
					# print('triple in line {}'.format(line))
					triplepass = True
				
			else:
				continue
		print(doubles, triples)
		line += 1

	checksum = doubles * triples
	print('Checksum = {}'.format(checksum))