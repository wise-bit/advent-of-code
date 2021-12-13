'''
@Author: wise-bit
@Date: 2021-12-XX
'''

from functools import reduce

sep = "\n" # separator

def lowPoint(g, p):
	x = p[0]
	y = p[1]
	v = g[y][x]
	if x > 0 and g[y][x-1] <= v: return False
	elif x < len(g[0])-1 and g[y][x+1] <= v: return False
	elif y > 0 and g[y-1][x] <= v: return False
	elif y < len(g)-1 and g[y+1][x] <= v: return False
	return True


v = []
a = []
c = 0 # counter
# temp = []

def block(x, y):
	return v[y][x] == True or a[y][x] == 9

def explore(x, y):
	global c
	# global temp
	c += 1
	# temp.append(a[y][x])
	v[y][x] = True
	if x > 0 and not block(x-1, y): explore(x-1, y)
	if x < len(a[0])-1 and not block(x+1, y):  explore(x+1, y)
	if y > 0 and not block(x, y-1): explore(x, y-1)
	if y < len(a)-1 and not block(x, y+1): explore(x, y+1)
	else: return

with open('input.txt', 'r') as file:
	a = [list(map(int, list(l))) for l in file.read().split(sep)]
	v = []
	for i in range(len(a)):
		t = []
		for j in range(len(a[i])):
			t.append(False)
		v.append(t)

	# Part 1

	# for i in range(len(a)):
	# 	for j in range(len(a[i])):
	# 		if lowPoint(a, (j, i)): c += a[i][j] + 1

	# print(c)

	mul_c = []
	for i in range(len(a)):
		for j in range(len(a[i])):	
			c = 0
			# temp = []
			if not block(j, i):
				explore(j, i)
			if c != 0:
				mul_c.append(c)
				# print(c, temp)

	print(reduce(lambda x, y: x*y, sorted(mul_c)[-3:]))

