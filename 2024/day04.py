sep = "\n"  # separator
res = 0  # result

a = []


def check_xmas(g, x, y, dx, dy, w):
  rs, cs = len(g), len(g[0])

  for i in range(len(w)):
    nx, ny = x + i * dx, y + i * dy
    if nx < 0 or ny < 0 or nx >= rs or ny >= cs or g[nx][ny] != w[i]:
      return False

  return True


def count_occ_1(g):
  rs, cs = len(g), len(g[0])
  cnt = 0

  directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

  for r in range(rs):
    for c in range(cs):
      for dx, dy in directions:
        if check_xmas(g, r, c, dx, dy, "XMAS"):
          cnt += 1

  return cnt


def count_occ_2(g):
  rs, cs = len(g), len(g[0])
  count = 0

  for r in range(rs):
    for c in range(cs):
      if g[r][c] == 'A':
        found_one = False
        if (0 <= r - 1 < rs and 0 <= c - 1 < cs and g[r - 1][c - 1] == 'M' and
                0 <= r + 1 < rs and 0 <= c + 1 < cs and g[r + 1][c + 1] == 'S'):
          found_one = True
        elif (0 <= r - 1 < rs and 0 <= c - 1 < cs and g[r - 1][c - 1] == 'S' and
                0 <= r + 1 < rs and 0 <= c + 1 < cs and g[r + 1][c + 1] == 'M'):
          found_one = True

        found_two = False
        if (0 <= r - 1 < rs and 0 <= c + 1 < cs and g[r - 1][c + 1] == 'M' and
                0 <= r + 1 < rs and 0 <= c - 1 < cs and g[r + 1][c - 1] == 'S'):
          found_two = True
        elif (0 <= r - 1 < rs and 0 <= c + 1 < cs and g[r - 1][c + 1] == 'S' and
                0 <= r + 1 < rs and 0 <= c - 1 < cs and g[r + 1][c - 1] == 'M'):
          found_two = True

        if found_one and found_two:
          count += 1

  return count


with open("input04.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    a.append(list(line))

print(count_occ_1(a))
print(count_occ_2(a))

print(res)
