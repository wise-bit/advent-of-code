from heapq import heappop, heappush

sep = "\n"

sol1 = 0
sol2 = 0


def show(g):
  rows, cols = len(g), len(g[0])
  for i in range(rows):
    for j in range(cols):
      print(g[i][j], end="")
    print()
  print()


def escape(g):
  rows, cols = len(g), len(g[0])
  dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  pq = [(0, 0, 0)]
  vis = set()

  while pq:
    cost, x, y = heappop(pq)

    if (x, y) == (rows - 1, cols - 1):
      return cost

    if (x, y) in vis:
      continue

    vis.add((x, y))

    for dx, dy in dirs:
      nx, ny = x + dx, y + dy
      if (
        0 <= nx < rows and 0 <= ny < cols and
        (nx, ny) not in vis and g[nx][ny] != '#'
      ):
        heappush(pq, (cost + 1, nx, ny))

  return -1


def reload_grid(all_vals, max_fallen):
  rows, cols = 71, 71
  g = []

  for _ in range(rows):
    g.append(["." for _ in range(cols)])

  fallen = 0
  for vals in all_vals[:max_fallen + 1]:
    x, y = int(vals[0]), int(vals[1])
    g[y][x] = "#"
    fallen += 1

  return g, all_vals[max_fallen]


def min_cutoff(all_vals):
  curr_max_fallen = 1025
  g, last_drop = reload_grid(all_vals, curr_max_fallen)

  escapable = escape(g) != -1

  while escapable:
    curr_max_fallen += 1
    g, last_drop = reload_grid(all_vals, curr_max_fallen)
    steps = escape(g)
    escapable = steps != -1

  return ",".join(str(x) for x in last_drop)


# main

all_vals = []
with open("input18.txt", "r") as file:
  lines = file.read().split(sep)
  for line in lines:
    vals = list(map(int, line.split(",")))
    all_vals.append(vals)

sol1 = escape(reload_grid(all_vals, 1024)[0])
sol2 = min_cutoff(all_vals)

print("part 1:", sol1)
print("part 2:", sol2)
