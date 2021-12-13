'''
@Author: wise-bit
@Date: 2021-12-XX
'''
with open('input.txt', 'r') as file:
	# Handle input
	inp = file.read().split("\n")
	split_index, dots, folds = 0, set(), []
	for line in inp:
		if line == "": break
		split_index += 1
		x, y = line.split(",")
		dots.add((int(x), int(y)))
	split_index += 1
	for line in inp[split_index:]:folds.append(line[11:].split("="))

	# Calculations for folds
	for fold in folds: 
		after = set()
		axis = fold[0]
		val = int(fold[1])
		for h in dots:
			if (axis == "x" and h[0] < val) or (axis == "y" and h[1] < val): after.add(h)
			else:
				if axis == "x": after.add((2*val - h[0], h[1]))
				else: after.add((h[0], 2*val - h[1]))
		dots = after
		print(len(dots))

	# Print 2d list
	highestX, highestY = 0, 0
	for d in dots: highestX, highestY = max(highestX, d[0]+1), max(highestY, d[1]+1)
	a = [[0]*highestX for i in range(highestY)]
	for c in dots: a[c[1]][c[0]] = 1
	for r in a: 
		for c in r: print(("#",".")[c==0], end="")
		print()
