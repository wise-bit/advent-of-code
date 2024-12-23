from collections import defaultdict

sep = "\n"


def build_adj_map(a):
  edge_set = set(a)
  adj_map = defaultdict(set)
  [adj_map[u].add(v) or adj_map[v].add(u) for u, v in edge_set]

  return adj_map


def part1(a):
  adj_map = build_adj_map(a)

  c3 = 0
  for u in adj_map:
    for v in adj_map[u]:
      if v > u:
        for w in adj_map[v]:
          if w > v and w in adj_map[u]:
            if any(node.startswith("t") for node in (u, v, w)):
              c3 += 1

  return c3


def clique(r, p, x, adj, cliques=None):
  if cliques is None:
    cliques = []

  # bron kerbosch

  if not p and not x:
    cliques.append(r)
    return

  for v in list(p):
    new_r = r | {v}
    new_p = p & adj[v]
    new_x = x & adj[v]

    clique(new_r, new_p, new_x, adj, cliques)

    p.remove(v)
    x.add(v)


def part2(a):
  adj_map = build_adj_map(a)

  cliques = []
  clique(set(), set(adj_map.keys()), set(), adj_map, cliques)

  return ",".join(sorted(sorted(cliques, key=len, reverse=True)[0]))


# main

a = []

with open("input23.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    a.append(tuple(line.split("-")))

# print(a)

sol1 = part1(a)
print("part 1:", sol1)

sol2 = part2(a)
print("part 2:", sol2)
