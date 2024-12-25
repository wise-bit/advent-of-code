sep = "\n"


def get_pins(schema, type):
  column_count = [0] * len(schema[0])
  sub_schema = schema[1:] if type == "lock" else schema[:-1]

  for row in sub_schema:
    for i, c in enumerate(row):
      if c == "#":
        column_count[i] += 1

  return column_count


def part1(locks, keys):
  lock_pins = []
  key_pins = []

  fit = 0

  for lock in locks:
    lock_pins.append(get_pins(lock, "lock"))

  for key in keys:
    key_pins.append(get_pins(key, "key"))

  for lock in lock_pins:
    for key in key_pins:
      if all(x + y <= 5 for x, y in zip(lock, key)):
        fit += 1

  return fit


def part2():
  return "Santa was satisfied!"


# main

locks = []
keys = []

with open("input25.txt", "r") as file:
  schematics = file.read().split(sep * 2)

  for scheme in schematics:
    if scheme[0] == "#":
      locks.append([list(x) for x in scheme.split(sep)])
    else:
      keys.append([list(x) for x in scheme.split(sep)])

sol1 = part1(locks, keys)
print("part 1:", sol1)

sol2 = part2()
print("part 2:", sol2)
