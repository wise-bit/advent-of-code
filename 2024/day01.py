sep = "\n"  # separator
c = 0  # counter

left = []
right = []

with open("input1.txt", "r") as file:
  lines = file.read().split(sep)
  
  for line in lines:
    entries = line.split()
    
    left.append(int(entries[0]))
    right.append(int(entries[1]))
    
left.sort()
right.sort()
  
cnt = len(left)

diff_sum = 0

for i in range(cnt):
  diff_sum += abs(left[i] - right[i])

# print(diff_sum)

similarity_score = 0

for x in left:
  similarity_score += x * right.count(x)

print(similarity_score)
  