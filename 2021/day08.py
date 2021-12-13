'''
@Author: wise-bit
@Date: 2021-12-XX
'''

sep = "\n" # separator

def so(word):
	return "".join(sorted(list(word)))

# Part 1

# with open('input.txt', 'r') as file:
# 	c = 0 # counter
# 	inp = file.read().split(sep)
# 	for line in inp:
# 		left, right = [x.split() for x in line.split(" | ")]
# 		for word in right:
# 			if len(word) < 5 or len(word) == 7: c += 1


# Part 2

def l(s):
	return len(s)

with open('input.txt', 'r') as file:
	c = 0
	inp = file.read().split(sep)
	for line in inp:
		specialmap = {}
		ans = ""
		backup5 = []
		backup6 = []
		track5 = []
		track6 = []
		mapping5 = {}
		four = set()
		eight = set()
		seven = set()
		three = set()
		left, right = [x.split() for x in line.split(" | ")]
		for w in left:
			if l(w) == 2: specialmap[so(w)] = 1
			elif l(w) == 3: seven = set(list(w)); specialmap[so(w)] = 7
			elif l(w) == 4: four = set(list(w)); specialmap[so(w)] = 4
			elif l(w) == 5: backup5.append(w); track5.append(set(list(w)))
			elif l(w) == 6: backup6.append(w); track6.append(set(list(w)))
			elif l(w) == 7: eight = set(list(w)); specialmap[so(w)] = 8

		s = track5[0]
		for w5 in track5: s = s.intersection(w5)
		for i in range(len(track5)): track5[i].difference_update(s)

		for i in range(len(track5)):
			score = 0
			for x in track5[i]:
				for j in range(len(track5)):
					if x in track5[j]: score += 1
			if score == 4: 
				specialmap[so(backup5[i])] = 3
				three = set(list(backup5[i]))
				track5.pop(i)
				backup5.pop(i)
				break

		for i in range(len(track5)):
			track5[i].difference_update(four)
			if len(track5[i]) == 0: specialmap[so(backup5[i])] = 5
			else: specialmap[so(backup5[i])] = 2

		for i in range(len(track6)):
			track6[i].difference_update(seven)

		for i in range(len(track6)):
			if len(track6[i]) == 4:
				specialmap[so(backup6[i])] = 6
				track6.pop(i)
				backup6.pop(i)
				break

		for i in range(len(track6)):
			track6[i].difference_update(three)

		for i in range(len(track6)):
			if len(track6[i]) == 2:
				specialmap[so(backup6[i])] = 0
			else:
				specialmap[so(backup6[i])] = 9

		# print(specialmap)

		
		for w in right:
			ans += str(specialmap[so(w)])
		# print(ans)
		c += int(ans)

	print(c)

'''
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''

