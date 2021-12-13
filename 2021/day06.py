'''
@Author: wise-bit
@Date: 2021-12-XX
'''

import time
from collections import deque 

sep = "\n" # separator
c = 0 # counter

with open('input.txt', 'r') as file:
	inp = file.read().split(sep)
	l = list(map(int, inp[0].split(",")))
	# queue = l

	d = {}
	for i in range(9):
		d[i] = 0
	for x in l:
		d[x] += 1

	# print(queue)

	r = 0

	start_time = time.time()
	for i in range(256):
		# for i in range(len(queue)):
		# 	if queue[i] == 0:
		# 		queue[i] = 6
		# 		queue.append(8)
		# 	else:
		# 		queue[i] = queue[i] - 1

		r = 0
		for k in range(9):
			if d[k] > 0:
				if k == 0:
					r = d[k]
					d[k] = 0
				else:
					d[k-1] = d[k]
					d[k] = 0
		d[6] += r
		d[8] += r

		# print(queue)
		# print(d)
		# print()

	c = 0
	for k in d:
		c += d[k]

	print("Runtime: %f s" % (time.time() - start_time))
	print(c)

	# for i in range(256):
	# 	for i in range(len(queue)):
	# 		if queue[i] == 0:
	# 			queue[i] = 6
	# 			queue.append(8)
	# 		else:
	# 			queue[i] = queue[i] - 1

	# 	print(queue)
	# print(len(queue))


# print(c)
