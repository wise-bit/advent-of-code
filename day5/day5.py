'''
@Author: wise-bit
@Date: 2020-12-05
'''
with open('input.txt', 'r') as file:
	c, highest, all_seats, inp = 0, 0, [], file.read().split("\n")
	for case in inp:
		m, n, a, b = 0, 127, 0, 7
		for x in case[:-3]:
			if x == "F": n = (m + n) // 2
			else: m = (m + n) // 2 + 1
		for x in case[-3:]:
			if x == "L": b = (a + b) // 2
			else: a = (a + b) // 2 + 1
		curr = m * 8 + a
		all_seats.append(curr)
		if curr > highest: highest = curr
	print("Highest seat: {}".format(highest))
	all_seats.sort()
	for i in range(1, len(all_seats) - 1):
		if all_seats[i+1] - all_seats[i] == 2: print("My seat: {}".format(all_seats[i]+1))
