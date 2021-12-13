'''
@Author: wise-bit
@Date: 2021-12-01
'''

sep = "\n" # separator
c = 0 # counter

inp = []

with open('input.txt', 'r') as file:
	inp = file.read().split(sep)
	# print(i)

	l = len(inp[0])

	# arr0 = []
	# arr1 = []

	# for i in range(l):
	# 	arr0.append(0)
	# 	arr1.append(0)

	# for x in inp:
	# 	for index in range(l):
	# 		if int(x[index]) == 0:
	# 			arr0[index] += 1
	# 		else:
	# 			arr1[index] += 1

	# print(arr0)
	# print(arr1)

# d = ""
# e = ""

# for i in range(l):
# 	if arr0[i] > arr1[i]:
# 		d += "0"
# 		e += "1"
# 	else:
# 		d += "1"
# 		e += "0"

# di = int(d, 2)
# ei = int(e, 2)

# print(di * ei)

# d = []
# e = []

# for i in range(l):
# 	if arr0[i] == arr1[i]:
# 		d.append(-1)
# 		e.append(-1)
# 	if arr0[i] > arr1[i]:
# 		d.append(0)
# 		e.append(1)
# 	else:
# 		d.append(1)
# 		e.append(0)

# o = 0
# c = 0

# print(d)
# print(e)

# print("--------")

indexx = 0
inp2 = inp

inp_orig = inp

while len(inp2) > 1:

	inp = inp2
	# print("---", inp)

	d = []
	e = []

	arr0 = []
	arr1 = []
	for i in range(l):
		arr0.append(0)
		arr1.append(0)

	for x in inp:
		for index in range(l):
			if int(x[index]) == 0:
				arr0[index] += 1
			else:
				arr1[index] += 1

	# print(arr0)
	# print(arr1)

	for i in range(l):
		if arr0[i] == arr1[i]:
			d.append(-1)
			e.append(0)
		elif arr0[i] > arr1[i]:
			d.append(0)
			e.append(1)
		else:
			d.append(1)
			e.append(0)

	# print(d)
	# print(e)

	if (indexx >= l): break

	inp2 = []
	# print("===", e[indexx])
	for x in inp:
		if int(x[indexx]) == d[indexx] or (d[indexx] == -1 and int(x[indexx]) == 1):
			# print(x[indexx],  d[indexx])
			inp2.append(x)

	# print(inp2)
	indexx += 1

inp = inp2

sum1 = int(inp[0], 2)






inp = inp_orig

indexx = 0
inp2 = inp

while len(inp2) > 1:

	inp = inp2
	# print("---", inp)

	d = []
	e = []

	arr0 = []
	arr1 = []
	for i in range(l):
		arr0.append(0)
		arr1.append(0)

	for x in inp:
		for index in range(l):
			if int(x[index]) == 0:
				arr0[index] += 1
			else:
				arr1[index] += 1

	# print(arr0)
	# print(arr1)

	for i in range(l):
		if arr0[i] == arr1[i]:
			d.append(0)
			e.append(-1)
		elif arr0[i] > arr1[i]:
			d.append(0)
			e.append(1)
		else:
			d.append(1)
			e.append(0)

	# print(d)
	# print(e)

	if (indexx >= l): break

	inp2 = []
	# print("===", e[indexx])
	for x in inp:
		if int(x[indexx]) == e[indexx] or (e[indexx] == -1 and int(x[indexx]) == 0):
			# print(x[indexx],  d[indexx])
			inp2.append(x)

	# print(inp2)
	indexx += 1

inp = inp2



sum2 = int(inp[0], 2)

print(sum1 * sum2)
