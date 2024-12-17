from heapq import heappop, heappush

sep = "\n"  # separator
sol = 0
g = []

dirs = {"r": (0, 1), "d": (1, 0), "l": (0, -1), "u": (-1, 0), }


def t_cost(c, n):
  dir_order = list(dirs.keys())
  ci, ni = dir_order.index(c), dir_order.index(n)
  turns = (ni - ci) % 4

  return 1000 * min(turns, 4 - turns)


def move(m, rev=False):
  s, e = None, None
  for r in range(len(m)):
    for c in range(len(m[0])):
      if m[r][c] == "S":
        s = (r, c)
      elif m[r][c] == "E":
        e = (r, c)

  if rev:
    s, e = e, s

  pq = []
  heappush(pq, (0, s[0], s[1], "r", []))

  vis = {}

  best_score = float("inf")
  best_paths = []

  while pq:
    sc, x, y, f, path = heappop(pq)

    if sc > best_score:
      continue

    if (x, y) == e:
      if sc < best_score:
        best_score = sc
        best_paths = [path + [(x, y)]]

      elif sc == best_score:
        best_paths.append(path + [(x, y)])

      continue

    if (x, y) in vis:
      prev_cost = vis[(x, y)]
      if sc - 1000 > prev_cost:
        continue

    vis[(x, y)] = sc

    for nd, (dx, dy) in dirs.items():
      if (x, y) != s and t_cost(f, nd) == 2000:
        continue

      nx, ny = x + dx, y + dy
      if 0 <= nx < len(m) and 0 <= ny < len(m[0]) and m[nx][ny] != "#":
        ns = sc + 1 + t_cost(f, nd)
        heappush(pq, (ns, nx, ny, nd, path + [(x, y)]))

  return best_score, best_paths, vis


with open("input16.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    g.append(list(line))


# main

best = move(g)
flattened = set([x for sub in best[1] for x in sub])

print(best[0])
print(len(flattened))
