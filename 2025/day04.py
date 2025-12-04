from copy import deepcopy

sep = "\n"


def fn():
  pass


def count_around(g, x, y):
  r, c = len(g), len(g[0])
  cnt = 0

  for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
      if 0 <= i < r and 0 <= j < c and not (i == x and j == y):
        if g[i][j] == "@":
          cnt += 1

  return cnt


# ---


def part1(a):
  # print(a)
  # print(count_around(a, 0, 0))

  r, c = len(a), len(a[0])
  sol = 0

  _g = deepcopy(a)

  for i in range(r):
    for j in range(c):
      if a[i][j] == "@":
        cnt = count_around(a, i, j)
        # print(cnt)

        if cnt < 4:
          sol += 1
          _g[i][j] = "x"

  # for row in _g:
  #   print("".join(row))
  
  # print("---")

  return sol


def part2(a):
  r, c = len(a), len(a[0])
  sol = 0

  _a = deepcopy(a)
  _g = deepcopy(a)

  last_removed = float("inf")

  while last_removed > 0:
    last_removed = 0

    for i in range(r):
      for j in range(c):
        if a[i][j] == "@":
          cnt = count_around(a, i, j)
          # print(cnt)

          if cnt < 4:
            last_removed += 1
            sol += 1

            _a[i][j] = "."
            _g[i][j] = "x"
    
    a = deepcopy(_a)

  return sol


if __name__ == "__main__":
  a = []

  with open("input04.txt", "r") as file:
    lines = file.read().split(sep)

    for line in lines:
      a.append(list(line))

  sol1 = part1(a)
  print("part 1:", sol1)

  sol2 = part2(a)
  print("part 2:", sol2)
