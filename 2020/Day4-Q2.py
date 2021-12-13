necessary = ['ecl', 'byr', 'iyr', 'pid', 'hgt', 'eyr', 'hcl']
count = 0

def verify_val(typ, val):
	if typ == "ecl":
		print("ecl failed")
	elif typ == "byr":
		return len(val) == 4 and 1920 <= int(val) <= 2002
	elif typ == "iyr":
		return len(val) == 4 and 2010 <= int(val) <= 2020
	elif typ == "pid":
		return len(val) == 9
	elif typ == "hgt":
		if not val[:-2].isdigit(): return False
		num = int(val[:-2])
		unit = val[-2:]
		return (unit == "cm" and 150 <= num <= 193) or (unit == "in" and 59 <= num <= 76)
	elif typ == "eyr":
		return len(val) == 4 and 2020 <= int(val) <= 2030
	elif typ == "hcl":
		return val[0] == "#" and len(val) == 7
	else: 
		return True


with open('Day4-inp1.txt') as f:
	keys = []
	values = []
	for l in f:
		if (l != "\n"):
			tmp = l.split(" ")
			for elem in tmp: 
				keys.append(elem.split(":")[0])
				values.append(elem.rstrip().split(":")[1])
		else:
			is_valid = True
			for n in necessary:
				if n not in keys: is_valid = False; break;
			for i in range(len(keys)):
				if not verify_val(keys[i], values[i]):
					print(keys, values)
					is_valid = False
					break
			if is_valid: count += 1
			keys = []
			values = []
	print(count)
