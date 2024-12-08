sep = "\n"  # separator
g = []


def find_points(coords, rows, cols, any_dist):
  def is_within_bounds(x, y):
    return 0 <= x < rows and 0 <= y < cols

  def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

  def is_on_same_line(p1, p2, point):
    dx1, dy1 = point[0] - p1[0], point[1] - p1[1]
    dx2, dy2 = p2[0] - point[0], p2[1] - point[1]
    return dx1 * dy2 == dx2 * dy1

  def is_valid_point(point, coords):
    align_count = 0
    for i, p1 in enumerate(coords):
      for j, p2 in enumerate(coords):
        if i != j and is_on_same_line(p1, p2, point):
          align_count += 1
          if align_count >= 1:
            return True

    return False

  results = []

  for i, p1 in enumerate(coords):
    for j, p2 in enumerate(coords):
      if i == j:
        continue

      for x in range(rows):
        for y in range(cols):
          point = (x, y)
          dist1 = distance(point, p1)
          dist2 = distance(point, p2)

          if (
              (
                (dist2 == 2 * dist1) or
                (any_dist and is_valid_point(point, coords))
              ) and
              is_within_bounds(x, y) and
              is_on_same_line(p1, p2, point)
          ):
            results.append(point)

  return results


def find_antinodes(f, any_dist=False):
  rows = len(f)
  cols = len(f[0])
  antennas = {}

  total_points = []

  for r in range(rows):
    for c in range(cols):
      char = f[r][c]
      if char.isalnum():
        if char not in antennas:
          antennas[char] = []
        antennas[char].append((r, c))

  for freq_list in antennas.values():
    points = find_points(freq_list, rows, cols, any_dist)
    total_points.extend(points)

  return total_points


with open("input08.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    g.append(list(line))


print(len(set(find_antinodes(g, True))))
