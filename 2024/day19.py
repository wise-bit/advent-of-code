sep = "\n"


def can_create(design, patterns):
  n = len(design) + 1
  cache = [False] * n
  cache[0] = True

  for sub_len in range(1, n):
    for pattern in patterns:
      p_len = len(pattern)

      if (
        sub_len >= p_len and cache[sub_len - p_len] and
        design[(sub_len - p_len):sub_len] == pattern
      ):
        cache[sub_len] = True
        break

  return cache[len(design)]


def count_options(design, patterns):
  n = len(design) + 1
  cache = [0] * n
  cache[0] = 1

  for i in range(1, n):
    for pattern in patterns:
      p_len = len(pattern)

      if i >= p_len and design[(i - p_len):i] == pattern:
        cache[i] += cache[i - p_len]

  return cache[len(design)]


def part1(patterns, designs):
  return len([design for design in designs if can_create(design, patterns)])


def part2(patterns, designs):
  res = []
  for design in designs:
    count = count_options(design, patterns)
    res.append(count)

  return sum(res)


# main

patterns = []
designs = []

with open("input19.txt", "r") as file:
  lines = file.read().split(sep)
  patterns = set(lines[0].split(", "))

  for line in lines[2:]:
    designs.append(line)

# print(patterns, designs)

sol1 = part1(patterns, designs)
print("part 1:", sol1)

sol2 = part2(patterns, designs)
print("part 2:", sol2)
