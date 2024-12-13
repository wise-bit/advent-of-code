sep = "\n"  # separator

sol = 0
a = []


def least_tokens(m):
  (dx1, dy1), (dx2, dy2), (px, py) = m

  res = float('inf')
  found = False

  for p1 in range(px // dx1 + 1):
    for p2 in range(py // dy2 + 1):
      x = p1 * dx1 + p2 * dx2
      y = p1 * dy1 + p2 * dy2

      if x == px and y == py:
        found = True
        res = min(res, p1 * 3 + p2 * 1)

  return res if found else -1


def least_tokens_fast(m):
  (dx1, dy1), (dx2, dy2), (px, py) = m
  (px, py) = (px + 10000000000000, py + 10000000000000)

  det = dx1 * dy2 - dx2 * dy1
  if det == 0:
    return -1

  for k in range(-abs(det), abs(det) + 1):
    p1 = (px * dy2 - py * dx2 + k * dx2 * dy2) // det
    p2 = (py * dx1 - px * dy1 + k * dx1 * dy1) // det

    if (
      p1 >= 0 and p2 >= 0 and
      p1 * dx1 + p2 * dx2 == px and p1 * dy1 + p2 * dy2 == py
    ):
      return p1 * 3 + p2

  return -1


with open("input13.txt", "r") as file:
  lines = file.read().split(sep)

  curr = [(-1, -1), (-1, -1), (-1, -1)]
  for i in range(len(lines)):
    line = lines[i]
    if i % 4 == 0:
      coords = line.split(": ")[1].split(", ")
      x = int(coords[0].split("+")[1])
      y = int(coords[1].split("+")[1])
      curr[0] = (x, y)
    elif i % 4 == 1:
      coords = line.split(": ")[1].split(", ")
      x = int(coords[0].split("+")[1])
      y = int(coords[1].split("+")[1])
      curr[1] = (x, y)
    elif i % 4 == 2:
      coords = line.split(": ")[1].split(", ")
      x = int(coords[0].split("=")[1])
      y = int(coords[1].split("=")[1])
      curr[2] = (x, y)
    else:
      a.append(curr)
      curr = [(-1, -1), (-1, -1), (-1, -1)]


sol = sum(least_tokens_fast(x) for x in a if least_tokens_fast(x) != -1)
print(sol)
