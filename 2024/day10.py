sep = "\n"  # separator

a = []
sol = 0


def trail_scores(g, x, y, curr, reached_set):
  h, w = len(g), len(g[0])

  if x < 0 or x >= h or y < 0 or y >= w or g[x][y] == '.':
    return len(reached_set)

  if g[x][y] != curr:
    return len(reached_set)

  if curr == 9:
    reached_set.add((x, y))
    return len(reached_set)

  temp = g[x][y]
  g[x][y] = '.'

  trail_scores(g, x + 1, y, curr + 1, reached_set)
  trail_scores(g, x - 1, y, curr + 1, reached_set)
  trail_scores(g, x, y + 1, curr + 1, reached_set)
  trail_scores(g, x, y - 1, curr + 1, reached_set)

  g[x][y] = temp

  return len(reached_set)


def trail_ratings(g, x, y, curr, rating_p):
  h, w = len(g), len(g[0])

  if x < 0 or x >= h or y < 0 or y >= w:
    return rating_p[0]

  if g[x][y] != curr:
    return rating_p[0]

  if curr == 9:
    rating_p[0] += 1
    return rating_p[0]

  temp = g[x][y]
  g[x][y] = -1

  trail_ratings(g, x + 1, y, curr + 1, rating_p)
  trail_ratings(g, x - 1, y, curr + 1, rating_p)
  trail_ratings(g, x, y + 1, curr + 1, rating_p)
  trail_ratings(g, x, y - 1, curr + 1, rating_p)

  g[x][y] = temp

  return rating_p[0]


def scan(g, rate=False):
  total = 0

  h, w = len(g), len(g[0])
  for i in range(h):
    for j in range(w):
      if g[i][j] == 0:
        if rate:
          total += trail_ratings(g, i, j, 0, [0])
        else:
          total += trail_scores(g, i, j, 0, set())

  return total


with open("input10.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    a.append(list(map(int, ["-1" if l == "." else l for l in list(line)])))


sol = scan(a)
print(sol)

sol = scan(a, True)
print(sol)
