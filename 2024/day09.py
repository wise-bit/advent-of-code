sep = "\n"  # separator

sol = 0
files = []
expanded = []

sample = "2333133121414131402"


def merge_blocks_combined(files):
  a = []
  curr = 0
  for i in range(len(files)):
    if i % 2 == 1:
      a.extend([-1] * files[i])
    else:
      a.extend([curr] * files[i])
      curr += 1
  return a


def merge_blocks_separated(files):
  a = []
  curr = 0
  for i in range(len(files)):
    if i % 2 == 1:
      a.append([-1] * files[i])
    else:
      a.append([curr] * files[i])
      curr += 1
  return a


def move_numbers_to_left(l):
  left = 0
  right = len(l) - 1
  while left < right:
    if l[right] == -1:
      right -= 1

    elif l[left] == -1:
      l[left], l[right] = l[right], l[left]
      left += 1

    else:
      left += 1

  return [x for x in l if x != -1]


def move_blocks_to_left(l):
  limit = len(l) - 1
  while limit > 0:
    # print(limit)
    left = 0
    right = limit

    while left < right:
      if len(l[right]) == 0 or (len(l[right]) > 0 and l[right][0] == -1):
        right -= 1

      elif (
        len(l[left]) > 0 and len(l[right]) > 0 and
        l[left][0] == -1 and len(l[left]) >= len(l[right])
      ):
        diff = len(l[left]) - len(l[right])
        temp = l[left]
        l[left] = l[right]
        l[right] = temp[:len(l[left])]

        l.insert(left + 1, [-1] * diff)
        # left, right = 0, len(l) - 1

      else:
        left += 1

    limit -= 1
    while len(l[limit]) == 0 or (len(l[limit]) > 0 and l[limit][0] == -1):
      limit -= 1

  return l


def checksum(l):
  s = 0
  for i in range(len(l)):
    if l[i] != -1:
      s += l[i] * i
  return s


with open("input09.txt", "r") as file:
  lines = file.read().split(sep)
  files = list(map(int, list(lines[0])))

# part 1
# expanded = merge_blocks_combined(files)
# expanded = move_numbers_to_left(expanded)

# part 2
expanded = merge_blocks_separated(files)
expanded = move_blocks_to_left(expanded)
expanded = sum(expanded, [])
print("".join(str(e) for e in expanded).replace("-1", "."))

sol = checksum(expanded)

print(sol)
