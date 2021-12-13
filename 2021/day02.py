'''
@Author: wise-bit
@Date: 2021-12-02
'''

sep = "\n" # separator
c = 0 # counter

with open('input.txt', 'r') as file:
	i = file.read().split(sep)
	h = d = 0
	aim = 0
	for x in i:
		a, b = x.split()
		b = int(b)
		if a[0] == "f":
			h += b
			d += b * aim
		elif a[0] == "u":
			aim -= b
		elif a[0] == "d":
			# d += b
			aim += b
		else:
			d = d

	print(h*d)

# print(c)
