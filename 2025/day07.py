from functools import cache


sep = "\n"
g = []


def find_all(l, s):
  a = []
  for i, x in enumerate(l):
    if x == s:
      a.append(i)

  return a


@cache
def rec_split(r, split_loc):
  # print(r, cnt, split_loc)

  if r == len(_g):
    return 1

  splits = find_all(_g[r], "^")

  if split_loc not in splits:
    return rec_split(r + 1, split_loc)

  left, right = split_loc - 1, split_loc + 1
  left_cnt, right_cnt = 0, 0

  if left > 0:
    left_cnt = rec_split(r + 1, left)
  if right < len(_g[0]):
    right_cnt = rec_split(r + 1, right)

  return left_cnt + right_cnt


def iter_split(g, split_loc):
  rs = len(g)
  cs = len(g[0])

  track = [0] * cs
  track[split_loc] = 1

  for r in range(rs):
    splits = find_all(g[r], "^")
    new_track = [0] * cs

    if not splits:
      new_track = track[:]

    else:
      for i in range(cs):
        if track[i]:
          if i not in splits:
            new_track[i] += track[i]

          else:
            v = track[i]
            if i - 1 >= 0:
              new_track[i - 1] += v
            if i + 1 < cs:
              new_track[i + 1] += v

    track = new_track

  return sum(track)


# ---


def part1(g):
  sol = 0
  start = g[0].index("S")
  # print(start)

  splitters = [start]

  for l in g[1:]:
    new_splitters = []
    splits = find_all(l, "^")

    if not splits:
      continue

    for index in splitters:
      if index in splits:
        sol += 1
        new_splitters.extend([index - 1, index + 1])
      else:
        new_splitters.append(index)
    
    splitters = list(set(new_splitters))
    # print(sol, splitters)

  return sol


def part2(g):
  global _g

  sol = 0
  split_loc = g[0].index("S")

  _g = g
  sol = rec_split(0, split_loc) + 1
  # sol = iter_split(g, split_loc)

  return sol


if __name__ == "__main__":
  g = []

  with open("input07.txt", "r") as file:
    lines = file.read().split(sep)

    for line in lines:
      g.append(list(line))

  sol1 = part1(g)
  print("part 1:", sol1)

  sol2 = part2(g)
  print("part 2:", sol2)
