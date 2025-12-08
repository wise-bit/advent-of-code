sep = "\n"


def dist(a, b):
  return ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)**0.5


def all_pair_distances(d):
  ks = list(d.keys())
  all_distances = []

  for i in range(len(ks)):
    for j in range(i+1, len(ks)):
      a, b = ks[i],ks[j]
      all_distances.append((a, b, dist(d[a], d[b])))

  return all_distances


def merge_overlapping(sets):
  merged_new = True

  while merged_new:
    merged_new = False
    new_sets = []

    while sets:
      s = sets.pop()
      merged_current = False

      for i, t in enumerate(sets):
        if s & t:
          sets[i] = s | t
          merged_new = True
          merged_current = True

          break

      if not merged_current:
        new_sets.append(s)

    sets = new_sets

  return sets


# ---


def part1_2(d, rounds = 10):
  # print(d)

  all_distances = all_pair_distances(d)
  all_distances.sort(key=lambda x: x[2])
  # print(all_distances[:3])

  circuits = []
  last_merged = (-1, -1)

  # index = 0
  added_boxes = set()
  

  # for _ in range(rounds):
  while (
    (rounds == -100 and (len(circuits) > 1 or len(added_boxes) < len(d))) or
    (rounds > 0)
  ):
    if rounds > 0:
      rounds -= 1

    # index += 1
    # print(last_merged)

    # debug
    # try:
    #   x, y = last_merged[0], last_merged[1]
    #   px, py = d[x], d[y]
    #   print(px, py)
    # except:
    #   pass

    a, b, _ = all_distances.pop(0)

    if not circuits:
      circuits.append({a, b})
      last_merged = (a, b)
      added_boxes.add(a)
      added_boxes.add(b)

    added_existing = False
    for c in circuits:
      if a in c or b in c:
        c.add(a)
        c.add(b)
        last_merged = (a, b)
        added_boxes.add(a)
        added_boxes.add(b)
        added_existing = True

        break

    if not added_existing:
      circuits.append({a, b})
      last_merged = (a, b)
      added_boxes.add(a)
      added_boxes.add(b)
    
    circuits = merge_overlapping(circuits)

  sol_arr = []
  sol1 = 1

  for c in circuits:
    # print(len(c))
    sol_arr.append(len(c))
  
  sol_arr.sort(reverse=True)
  
  for s in sol_arr[:3]:
    sol1 *= s

  # print(index)

  x, y = last_merged[0], last_merged[1]
  px, py = d[x], d[y]
  # print(px, py)

  sol2 = px[0] * py[0]

  return sol1, sol2



def part2():
  pass


if __name__ == "__main__":
  d = dict()

  with open("input08.txt", "r") as file:
    lines = file.read().split(sep)

    for i, line in enumerate(lines):
      d[i] = tuple(map(int, line.split(",")))

  sol1, _ = part1_2(d, 1000)
  _, sol2 = part1_2(d, -100)

  print("part 1:", sol1)
  print("part 2:", sol2)
