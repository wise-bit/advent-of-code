count = 0
index = 0

with open('Day3-inp1.txt') as f:
	for l in f:
		s = l.rstrip('\n')
		if index == 0:
			index += 3
		else:
			if s[index % (len(s))] == "#":
				count += 1
			index += 3
	print(count)
