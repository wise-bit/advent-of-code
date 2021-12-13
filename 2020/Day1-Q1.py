a = []
d = {}

sol = 2020

with open('inp1.txt') as f:
	for l in f:
		a.append(int(l))

for x in a:
	if sol - x in d:
		print(x * (sol-x))
	else:
		d[x]=1