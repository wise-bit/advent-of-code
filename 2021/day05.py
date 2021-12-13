'''
@Author: wise-bit
@Date: 2021-12-XX
'''

sep = "\n" # separator
c = 0 # counter

with open('input.txt', 'r') as file:
	inp = file.read().split(sep)

	max_x = 0
	max_y = 0

	for line in inp:
		s, e = line.split(" -> ")
		xi, yi = map(int, s.split(","))
		xj, yj = map(int, e.split(","))
		# print(xi, yi)
		if xi >= max_x: max_x = xi+1
		if xj >= max_x: max_x = xj+1
		if yi >= max_y: max_y = yi+1
		if yj >= max_y: max_y = yj+1

	# print(max_x, max_y)

	a = []
	for i in range(max_y):
		l = []
		for j in range(max_x):
			l.append(0)
		a.append(l)
	# print("------", max_x, max_y)

	for line in inp:
		s, e = line.split(" -> ")
		xi, yi = map(int, s.split(","))
		xj, yj = map(int, e.split(","))

		if yj - yi == xj - xi:
			top_left_x, bottom_right_x = min(xi, xj), max(xi, xj)
			top_left_y, bottom_right_y = min(yi, yj), max(yi, yj)
			# print(top_left_x, bottom_right_x)
			diff = bottom_right_x - top_left_x
			for i in range(diff + 1):
				a[top_left_y + i][top_left_x + i] += 1

		elif yj - yi == -(xj - xi):
			top_right_x, bottom_left_x = max(xi, xj), min(xi, xj)
			top_right_y, bottom_left_y = min(yi, yj), max(yi, yj)
			diff = top_right_x - bottom_left_x
			for i in range(diff + 1):
				a[bottom_left_y - i][bottom_left_x + i] += 1

		elif xi == xj:
			start_y, end_y = min(yi, yj), max(yi, yj)
			for i in range(start_y, end_y+1):
				a[i][xi] += 1
		
		elif yi == yj:
			start_x, end_x = min(xi, xj), max(xi, xj)
			for i in range(start_x, end_x+1):
				a[yi][i] += 1


	for i in range(max_y):
		for j in range(max_x):
			if a[i][j] == 0:
				print(".", end="")
			else:
				print(a[i][j], end="")
		print()

	c = 0

	for i in range(max_y):
		for j in range(max_x):
			if a[i][j] > 1:
				c += 1
			# print(a[i][j], end=" ")
		# print()

	print(c)

