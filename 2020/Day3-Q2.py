def checkTrees(right, down):
	count = 0
	index = 0
	skipper = 0
	with open('Day3-inp1.txt') as f:
		for l in f:
			if skipper % down == 0:
				s = l.rstrip('\n')
				if index == 0:
					index += right
				else:
					if s[index % (len(s))] == "#":
						count += 1
					index += right
			skipper += 1
	return count

m = 1

for i in range(1, 8, 2):
	# print(i)
	print(checkTrees(i, 1))
	m *= checkTrees(i, 1)


m *= checkTrees(1, 2)

print(m)
