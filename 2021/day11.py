'''
@Author: wise-bit
@Date: 2021-12-XX
'''
with open('input.txt', 'r') as file:
	total_flashes = 0 # counter
	a = [list(map(int, list(l))) for l in file.read().split("\n")]

	total_steps = 200
	total_so_far = 0

	while True:
		total_steps -= 1
		total_so_far += 1
		flashes_this_round = 0

		v = []
		for i in range(len(a)):
			temp = []
			for j in range(len(a[i])): temp.append(0)
			v.append(temp)

		for i in range(len(a)):
			for j in range(len(a[i])):
				a[i][j] += 1

		flashes = True
		while flashes == True:
			flashes = False

			for i in range(len(a)):
				for j in range(len(a[i])):
					if a[i][j] > 9 and v[i][j] == 0:
						total_flashes += 1
						flashes_this_round += 1
						v[i][j] = 1
						flashes = True
						for i_ in range(i-1, i+2):
							for j_ in range(j-1, j+2):
								if len(a) > i_ >= 0 and len(a[i]) > j_ >= 0:
									a[i_][j_] += 1

		for i in range(len(a)):
			for j in range(len(a[i])):
				if a[i][j] > 9: a[i][j] = 0

		if flashes_this_round == len(a) * len(a[0]):
			print("All flash first at: " + str(total_so_far)); break

	# print("Total flashes:" + str(total_flashes))
