necessary = ['ecl', 'byr', 'iyr', 'pid', 'hgt', 'eyr', 'hcl']
count = 0

with open('Day4-inp1.txt') as f:
	keys = []
	for l in f:
		if (l != "\n"):
			tmp = l.split(" ")
			for elem in tmp: keys.append(elem.split(":")[0])
		else:
			is_valid = True
			for n in necessary:
				if n not in keys: is_valid = False; break;
			if is_valid: count += 1
			keys = []
	print(count)
