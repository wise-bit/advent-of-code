sep = "\n"


def has_twice_repeat(s):
  l = len(s)
  return l % 2 == 0 and s[:l//2] == s[l//2:]


def has_any_repeat(s):
  return s in (s*2)[1:-1]


# ---


def part1(a):
  sol = 0
  for t in a:
    for n in range(t[0], t[1]+1):
      if has_twice_repeat(str(n)):
        # print(n, t)
        sol += n

  return sol


def part2():
  sol = 0
  for t in a:
    for n in range(t[0], t[1]+1):
      if has_any_repeat(str(n)):
        # print(n, t)
        sol += n

  return sol


# main

a = []

with open("input02.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    ranges = line.rstrip(",").split(",")
    for r in ranges:
      x, y = r.split("-")
      a.append((int(x), int(y)))


sol1 = part1(a)
print("part 1:", sol1)

sol2 = part2()
print("part 2:", sol2)
