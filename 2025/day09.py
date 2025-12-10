sep = "\n"


def area_rect(p1, p2):
  x1, x2 = sorted([p1[0], p2[0]])
  y1, y2 = sorted([p1[1], p2[1]])
  x2 += 1
  y2 += 1

  return (x2 - x1) * (y2 - y1)


def rect_corners(p1, p2):
  x1, x2 = sorted([p1[0], p2[0]])
  y1, y2 = sorted([p1[1], p2[1]])

  return ((x1, y1), (x2, y2), (x1, y2), (x2, y1))


def rect_perimeter(x1, y1, x2, y2):
  points = set()

  for x in range(x1, x2 + 1):
    points.add((x, y1))
    points.add((x, y2))

  for y in range(y1 + 1, y2):
    points.add((x1, y))
    points.add((x2, y))

  return points


# def gen_all_loop_points(a):
#   ps = set()
#   for i in range(100000):
#     for j in range(100000):
#       ps.add((j, i))
  
#   return ps


def check_point_in_loop(x, y, a):
  # case 1 - point
  if (x, y) in a:
    return True

  n = len(a)

  # case 2 - edge
  for i in range(n):
    next_i = (i + 1) % n

    x1,y1 = a[i]
    x2,y2 = a[next_i]

    if x1 == x2 and x == x1 and min(y1,y2) <= y <= max(y1,y2):
      return True
    if y1 == y2 and y == y1 and min(x1,x2) <= x <= max(x1,x2):
      return True
  
  # case 3 - inside
  valid = False
  crosses = 0

  for i in range(n):
    next_i = (i + 1) % n

    x1, y1 = a[i]
    x2, y2 = a[next_i]

    if (((y1 > y) and not (y2 > y)) or ((y1 <= y) and (y2 > y))) and (y2 != y1):
      m = (x2 - x1) / (y2 - y1)
      b = x1
      x_intersection = m * (y - y1) + b

      if x_intersection >= x:
        crosses += 1
  
  valid = crosses % 2 == 1

  return valid


# ---


def part1(a):
  sol = -1

  for i in range(len(a)):
    for j in range(i+1, len(a)):
      curr = area_rect(a[i], a[j])
      sol = max(sol, curr)

  return sol


def part2(a):
  memo = {}
  
  # nested fn
  def cached_check(x, y):
    if (x, y) not in memo:
      memo[(x, y)] = check_point_in_loop(x, y, a)
    
    return memo[(x, y)]

  sol = -1
  sol_corners = None

  for i in range(len(a)):
    for j in range(i+1, len(a)):
      corners = rect_corners(a[i], a[j])
      curr_area = area_rect(a[i], a[j])

      if not all(cached_check(x, y) for x, y in corners):
        continue

      if curr_area < sol:
        continue

      if not all(check_point_in_loop(x, y, a) for x, y in corners):
        continue
    
      x1, y1, x2, y2 = corners[0][0], corners[0][1], corners[1][0], corners[1][1]
      if not all(check_point_in_loop(x, y, a) for x, y in rect_perimeter(x1, y1, x2, y2)):
        continue

      # good = True
      # for y in range(corners[0][1], corners[1][1] + 1):
      #   for x in range(corners[0][0], corners[1][0] + 1):
      #     if not check_point_in_loop(x , y, a):
      #       good = False
      #       break

      #   if not good:
      #     break

      # if not good:
      #   continue

      if curr_area > sol:
        sol = curr_area
        sol_corners = (a[i], a[j])

  print(sol_corners)
  return sol


def part2_optimize_test(a):
  xs = sorted(set(p[0] for p in a))
  ys = sorted(set(p[1] for p in a))
  x_index = {x:i for i,x in enumerate(xs)}
  y_index = {y:i for i,y in enumerate(ys)}

  w, h = len(xs), len(ys)
  inside = [[0]*h for _ in range(w)]

  for i, x in enumerate(xs):
    for j, y in enumerate(ys):
      if check_point_in_loop(x, y, a):
        inside[i][j] = 1

  pre = [[0]*(h+1) for _ in range(w + 1)]
  for i in range(1, w+1):
    for j in range(1, h+1):
      pre[i][j] = inside[i - 1][j - 1] + pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1]

  def rect_sum(x1, y1, x2, y2):
    xi1, yi1 = x_index[x1], y_index[y1]
    xi2, yi2 = x_index[x2], y_index[y2]
    return pre[xi2 + 1][yi2 + 1] - pre[xi1][yi2 + 1] - pre[xi2 + 1][yi1] + pre[xi1][yi1]

  sol = -1
  # sol_corners = None
  n = len(a)

  for i in range(n):
    for j in range(i+1, n):
      p1, p2, _, _ = rect_corners(a[i], a[j])
      if p1[0] == p2[0] or p1[1] == p2[1]:
        continue

      total_ps = (x_index[p2[0]] - x_index[p1[0]] + 1) * (y_index[p2[1]] - y_index[p1[1]] + 1)

      if rect_sum(p1[0], p1[1], p2[0], p2[1]) != total_ps:
        continue

      curr_area = area_rect(a[i], a[j])
      if curr_area > sol:
        sol = curr_area
        # sol_corners = (a[i], a[j])

  # print(sol_corners)
  return sol


if __name__ == "__main__":
  a = []

  with open("input09.txt", "r") as file:
    lines = file.read().split(sep)

    for line in lines:
      a.append(tuple(map(int, line.split(","))))

  sol1 = part1(a)
  print("part 1:", sol1)

  sol2 = part2(a)
  print("part 2:", sol2)
