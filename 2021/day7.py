'''
@Author: wise-bit
@Date: 2021-12-XX
'''

from statistics import *

sep = "\n" # separator

# with open('input.txt', 'r') as file:
#   c = 0 # counter
# 	inp = file.read().split(sep)
# 	# print(i)
# 	a = list(map(int, inp[0].split(",")))
# 	# print(a)

# 	mi, ma = min(a), max(a)
# 	print(mi, ma)

# 	m = median(a)

# 	for x in a:
# 		c += abs(int(m) - x)


# print(c)

def fuel_cost(levels):
	return (levels**2+levels)//2

# print(fuel_cost(4))

def calc_total_cost(l, level):
	c = 0
	for x in l:
		c += fuel_cost(abs(int(level) - x))
	return c


with open('input.txt', 'r') as file:
	inp = file.read().split(sep)
	# print(i)
	a = list(map(int, inp[0].split(",")))
	# print(a)

	mi, ma = min(a), max(a)
	# print(mi, ma)

	l2 = []

	for i in range(mi, ma+1):
		k = calc_total_cost(a, i)
		l2.append(k)

	print(min(l2))

