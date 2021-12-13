'''
@Author: wise-bit
@Date: 2021-12-XX
'''
adjacency_list, count, visited = {}, 0, {}
def explore(v, path, usedTwice):
	global count
	for cave in adjacency_list[v]:
		if cave == "end": count += 1; # print(",".join(list(path)))
		else:
			if cave.isupper():
				visited[cave] += 1; path += cave; 
				explore(cave, path, usedTwice); 
				visited[cave] -= 1; path = path[:-1] 
			elif cave.islower() and visited[cave] == 1 and not usedTwice and cave not in ["start", "end"]:
				visited[cave] += 1; 
				path += cave; explore(cave, path, True); visited[cave] -= 1; 
				path = path[:-1] 
			elif cave.islower() and visited[cave] == 0 and cave not in ["start", "end"]:
				visited[cave] += 1; path += cave; 
				explore(cave, path, usedTwice); visited[cave] -= 1; 
				path = path[:-1] 
	return

def add_adjacency(a, b):
	if a not in adjacency_list: adjacency_list[a] = [b]
	else: adjacency_list[a].append(b)
	if b not in adjacency_list: adjacency_list[b] = [a]
	else: adjacency_list[b].append(a)

with open('input.txt', 'r') as file:
	for x in file.read().split("\n"):
		line = x.split("-")
		add_adjacency(line[0], line[1])
		visited[line[0]], visited[line[1]] = 0, 0
	# print(adjacency_list)
	explore("start", "", False)
	print(count)
