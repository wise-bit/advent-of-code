a = []

with open('inp1.txt') as f:
    for l in f:
		a.append(int(l))

for x in a:
	for y in a:
		for z in a:
			if x + y + z == 2020:
				print(x*y*z)