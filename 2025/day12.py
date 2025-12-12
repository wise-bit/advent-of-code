# from copy import deepcopy


sep = "\n"


def rotate(a):
  _a = [list(r) for r in zip(*reversed(a))]
  return _a


def print_a(a):
  for l in a:
    print("".join("#" if x else "." for x in l))
  print()


def check_fit(g, a, x, y):
  valid = True
  for i, r in enumerate(a):
    for j, v in enumerate(r):
      if g[y + i][x + j] and v:
        valid = False
        break

    if not valid:
      break

  return valid


def add_shape(g, a, x, y):
  for i, r in enumerate(a):
    for j, v in enumerate(r):
      if v:
        g[y + i][x + j] = True


def remove_shape(g, a, x, y):
  for i, r in enumerate(a):
    for j, v in enumerate(r):
      if v:
        g[y + i][x + j] = False


def rec_can_add_all_shapes(g, shapes, shape_list, shape_i = 0):
  if shape_i >= len(shape_list):
    return True

  shape = shapes[shape_list[shape_i]]

  for _ in range(4):
    for i in range(len(g) - len(shape) + 1):
      for j in range(len(g[0]) - len(shape[0]) + 1):
        if check_fit(g, shape, j, i):
          add_shape(g, shape, j, i)

          if rec_can_add_all_shapes(g, shapes, shape_list, shape_i + 1):
            return True

          remove_shape(g, shape, j, i)

    shape = rotate(shape)

  return False


# ---


def part1(shapes, regions):
  sol = 0

  for region in regions:
    width, height, counts = region

    total_required = 0
    total_available = width * height

    for i, count in enumerate(counts):
      shape_area = sum(sum(row) for row in shapes[i])
      total_required += shape_area * count

    sol += total_required <= total_available

    # g = []
    # for _ in range(region[1]):
    #   g.append([False] * region[0])

    # shape_list = []
    # for i, v in enumerate(region[2]):
    #   shape_list.extend([i] * v)

    # -- debug
    # test_shape = rotate(shapes[shape_list[0]])
    # print(check_fit(g, test_shape, 0, 0))
    # add_shape(g, test_shape, 0, 0)
    # print(check_fit(g, test_shape, 0, 0))
    # print_a(g)

    # print(g, shapes, shape_list)
    # print(rec_can_add_all_shapes(g, shapes, shape_list))

    # break
  
  return sol


def part2():
  pass


if __name__ == "__main__":
  shapes = []
  regions = []

  with open("input12.txt", "r") as file:
    parts = file.read().split(sep * 2)

    regions_plus = parts[-1].split(sep)
    regions = []
    for region_raw in regions_plus:
      dims_raw = region_raw.split(": ")
      x, y = map(int, dims_raw[0].split("x"))
      req = tuple(map(int, dims_raw[1].split()))
      regions.append((x, y, req))

    shapes_plus = [part.split(sep) for part in parts[:-1]]
    shapes = dict()
    for shape in shapes_plus:
      shapes[int(shape[0][:-1])] = [[x == "#" for x in line] for line in shape[1:]]

  sol1 = part1(shapes, regions)
  print("part 1:", sol1)

  sol2 = part2()
  print("part 2:", sol2)
