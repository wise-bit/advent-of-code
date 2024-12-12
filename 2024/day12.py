from collections import deque

sep = "\n"  # separator

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
g = []


def bound(x, y, g):
  return 0 <= x < len(g) and 0 <= y < len(g[0])


def count_sides(t):
  visited = set()
  c = 0
  for p in t:
    if p in visited:
      continue

    c += 1

    queue = [(p[0], p[1])]
    old_dx, old_dy = p[2], p[3]
    visited.add(p)

    for x, y in queue:
      for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (
          (nx, ny, old_dx, old_dy) not in visited and
          (nx, ny, old_dx, old_dy) in t
        ):
          queue.append((nx, ny))
          visited.add((nx, ny, old_dx, old_dy))

  return c


def flood_fill(g, r, c, v, seen):
  t = set()
  q = deque([(r, c)])
  seen.add((r, c))
  area, peri = 0, 0

  while q:
    x, y = q.popleft()
    area += 1
    p = 0

    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
      nx, ny = x + dx, y + dy
      if bound(nx, ny, g) and g[nx][ny] == v:
        if (nx, ny) not in seen:
          seen.add((nx, ny))
          q.append((nx, ny))
      else:
        p += 1
        t.add((nx, ny, dx, dy))

    peri += p

  sides = count_sides(t)
  # print(t, "::", sides)
  return area, peri, sides


def fence_price(g, sides=False):
  seen = set()
  res = 0

  for r in range(len(g)):
    for c in range(len(g[0])):
      if (r, c) not in seen:
        a, p, s = flood_fill(g, r, c, g[r][c], seen)
        if sides:
          res += a * s
        else:
          res += a * p

  return res


with open("input12.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    g.append(list(line))

print(fence_price(g, False))  # Day 1
print(fence_price(g, True))  # Day 2
