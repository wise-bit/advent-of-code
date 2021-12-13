'''
@Author: wise-bit
@Date: 2021-12-XX
'''
from statistics import median

opens = ["(", "[", "{", "<"]
closes = [")", "]", "}", ">"]
points = [3, 57, 1197, 25137]
points2 = [1, 2, 3, 4]

def check(s):
	st = []
	for i in s:
		if i in opens:
			st.append(i)
		elif i in closes:
			p = closes.index(i)
			if ((len(st) > 0) and
				(opens[p] == st[len(st)-1])):
				st.pop()
			else:
				return points[p]
	if len(st) == 0:
		return 0
	return 0

def check2(s):
	st = []
	for i in s:
		if i in opens:
			st.append(i)
		elif i in closes:
			p = closes.index(i)
			if ((len(st) > 0) and
				(opens[p] == st[len(st)-1])):
				st.pop()
			else:
				return ""
	if len(st) == 0:
		return ""
	sol = []
	for i in st:
		sol.insert(0, closes[opens.index(i)])
	return "".join(sol)

with open('input.txt', 'r') as file:
	inp = file.read().split("\n")

	total_score = 0
	individual_scores2 = []

	for x in inp: 

		this_score = 0
		sc = check2(x)
		for x in sc:
			this_score = this_score * 5 + points2[closes.index(x)]

		if this_score != 0: individual_scores2.append(this_score)

	individual_scores2.sort()
	print(int(median(individual_scores2)))

	# print(total_score)
