sep = "\n"


def evolve(n):
  n2 = ((n * 64) ^ n) % 16777216
  n3 = ((n2 // 32) ^ n2) % 16777216
  n4 = ((n3 * 2048) ^ n3) % 16777216

  return n4


def part1(a, r):
  f = []
  for x in a:
    n = x
    for _ in range(r):
      n = evolve(n)
    f.append(n)

  return sum(f)


def part2(a, r):
  ds = []
  for x in a:
    d = []
    n = x
    u = n % 10
    u2 = 0
    for _ in range(r):
      n2 = evolve(n)
      u = n % 10
      u2 = n2 % 10

      d.append((u2, u2 - u))
      n = n2

    ds.append(d)

  seqs = {}

  for p in range(len(ds)):
    vis = set()

    for i in range(4, r):
      seq = ",".join([str(s[1]) for s in ds[p][(i - 4):i]])
      best = ds[p][i - 1][0]

      if seq not in vis:
        seqs[seq] = seqs.get(seq, 0) + best

      vis.add(seq)

  best_seq = max(seqs, key=seqs.get)
  print("p2 best:", best_seq)

  return seqs[best_seq]


# main
a = []

with open("input22.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    a.append(int(line))

# print(a)

sol1 = part1(a, 2000)
print("part 1:", sol1)

sol2 = part2(a, 2000)
print("part 2:", sol2)
