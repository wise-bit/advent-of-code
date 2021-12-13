count = 0

with open('Day2-inp1.txt') as f:
	for l in f:
		l_spl = l.split(" ")

		range_spl = l_spl[0].split("-")
		low = int(range_spl[0])
		high = int(range_spl[1])

		letter = l_spl[1][0]

		line = l_spl[2][:-1]
		
		if (low <= line.count(letter) <= high): count += 1

	print(count)