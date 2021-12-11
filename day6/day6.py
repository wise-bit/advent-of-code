'''
@Author: wise-bit
@Date: 2021-12-XX
'''
with open('input.txt', 'r') as file:
	c = 0
	every_count = 0
	for x in file.read().split("\n\n"):
		each = x.split("\n")
		s = set(list(x.replace("\n", "")))
		for x in s:
			c2 = 0
			for e in each:
				if x in e: c2 += 1
			if c2 == len(each): every_count += 1
		c += len(s)
	print(every_count)
