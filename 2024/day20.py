from heapq import heappop, heappush

sep = "\n"


def is_valid(g, x, y):
  return 0 <= x < len(g) and 0 <= y < len(g[0]) and g[x][y] != '#'


def move(g, start, end):
  rows, cols = len(g), len(g[0])
  dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  pq = [(0, start[0], start[1])]

  vis = set()
  pathing = {}

  while pq:
    cost, x, y = heappop(pq)

    if (x, y) == end:
      path = []
      curr = (x, y)

      while curr in pathing:
        path.append(curr)
        curr = pathing[curr]

      path.append(start)
      return path[::-1]

    if (x, y) in vis:
      continue

    vis.add((x, y))

    for dx, dy in dirs:
      nx, ny = x + dx, y + dy
      if (
          0 <= nx < rows and 0 <= ny < cols and
          (nx, ny) not in vis and g[nx][ny] != '#'
      ):
        pathing[(nx, ny)] = (x, y)
        heappush(pq, (cost + 1, nx, ny))

  return []


def move_disable_test(g, start, end, total_dis):
  rows, cols = len(g), len(g[0])
  dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  pq = [(0, start[0], start[1], 0, False, [])]
  vis = set()
  results = []

  while pq:
    cost, x, y, dis_cnt, sequence, dis_path = heappop(pq)
    state = (x, y, dis_cnt, sequence, tuple(dis_path))

    if state in vis:
      continue

    vis.add(state)

    if (x, y) == end:
      results.append([cost, dis_path])
      continue

    for dx, dy in dirs:
      nx, ny = x + dx, y + dy

      if 0 <= nx < rows and 0 <= ny < cols:
        if g[nx][ny] == '#':
          if dis_cnt < total_dis - 1 and (sequence or dis_cnt == 0):
            new_path = dis_path + [(nx, ny)]
            heappush(pq, (cost + 1, nx, ny, dis_cnt + 1, True, new_path))

        else:
          heappush(pq, (cost + 1, nx, ny, dis_cnt, False, dis_path))

  return [r for r in results if r[0] < move(g, start, end)]


def manhattan(p1, p2):
  return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def scan_disable(g, start, end, allowed):
  steps = move(g, start, end)

  count_skips = 0
  for i in range(len(steps)):
    for j in range(i + 100, len(steps)):
      man = manhattan(steps[i], steps[j])

      if (j - i) - man >= 100 and man <= allowed:
        count_skips += 1

  return count_skips


def part1(g, start, end):
  return scan_disable(g, start, end, 2)


def part2(g, start, end):
  return scan_disable(g, start, end, 20)


# main

g = []
start = (-1, -1)
end = (-1, -1)

with open("input20.txt", "r") as file:
  lines = file.read().split(sep)
  y_incr = 0

  for line in lines:
    if "S" in line:
      start = (y_incr, line.index("S"))

    if "E" in line:
      end = (y_incr, line.index("E"))

    g.append(list(line.replace("S", ".").replace("E", ".")))

    y_incr += 1

# print(start, end, g)

sol1 = part1(g, start, end)
print("part 1:", sol1)

sol2 = part2(g, start, end)
print("part 2:", sol2)
