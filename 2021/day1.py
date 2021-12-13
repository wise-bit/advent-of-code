'''
@Author: wise-bit
@Date: 2021-12-01
'''

separator = "\n"

c = 0

with open('input.txt', 'r') as file:
	inp = file.read().split(separator)
	prev = int(inp[0]) + int(inp[1]) + int(inp[2])
	for i in range(0, len(inp) - 2):
		n = int(inp[i]) + int(inp[i+1]) + int(inp[i+2])
		if n > prev: 
			c += 1
		prev = n

	# print(inp)

print(c)
