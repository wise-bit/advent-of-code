import numpy as np

sep = "\n"


def transform_moves(moves, d=True):
  if not d:
    return list(map(float, [x.replace("A", "0.5") for x in list(moves)]))

  d_grid_map = {"^": 0, "A": 0.5, "<": -4, "v": -3, ">": -2}
  return list(map(lambda x: d_grid_map[x], list(moves)))


def init_gen_moves(s, e, g, path=None):
  if path is None:
    path = []

  if s == e:
    return [path]

  sr, sc = s
  er, ec = e
  moves = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
  all_paths = []

  for m, (dr, dc) in moves.items():
    nr, nc = sr + dr, sc + dc

    if (
      0 <= nr < len(g) and 0 <= nc < len(g[0]) and g[nr][nc] != -1 and
      (
        (m == '^' and sr > er) or (m == 'v' and sr < er) or
        (m == '<' and sc > ec) or (m == '>' and sc < ec)
      )
    ):
      new_path = path + [m]
      all_paths.extend(init_gen_moves((nr, nc), e, g, new_path))

  return all_paths


def init_filter_moves(moves):
  max_repeats = 0
  collect = []

  for m in moves:
    for i in range(len(m)):
      curr_repeats = 1

      for j in range(i + 1, len(m)):
        if m[i] != m[j]:
          break
        curr_repeats += 1

      if max_repeats == curr_repeats:
        collect.append(m)

      elif max_repeats < curr_repeats:
        max_repeats = curr_repeats
        collect = [m]

  return collect


def init_move(start, end, grid):
  i = 0
  while start < grid[i][0]:
    i += 1

  j = 0
  while end < grid[j][0]:
    j += 1

  p1 = (i, grid[i].index(start))
  p2 = (j, grid[j].index(end))

  init_moves = init_gen_moves(p1, p2, grid)
  init_moves = init_filter_moves(init_moves)
  init_moves_str = list(set(["".join(p) for p in init_moves]))

  return init_moves_str


def build_seq(keys, graph, index=0, prev_key=0.5, curr_path="", res=None):
  if res is None:
    res = []

  if index == len(keys):
    res.append(curr_path)
    return res

  curr_key = keys[index]
  paths = graph.get((prev_key, curr_key), [])

  if not paths:
    build_seq(keys, graph, index + 1, curr_key, curr_path + "A", res)

  else:
    for path in paths:
      build_seq(keys, graph, index + 1, curr_key, curr_path + path + "A", res)

  return res


def shortest_seq(keys, depth, cache, graph):
  if depth == 0:
    return len(keys)

  key_str = ",".join(str(x) for x in keys)

  if (key_str, depth) in cache:
    return cache[(key_str, depth)]

  keys_split = []
  temp = []
  for k in keys:
    if k != 0.5:
      temp.append(k)
    else:
      if temp:
        keys_split.append(temp + [0.5])
        temp = []
  if temp:
    keys_split.append(temp)

  total = 0
  for key in keys_split:
    sub_seq = build_seq(key, graph)
    min_seq_len = float("inf")
    for seq in sub_seq:
      sub_t_seq = transform_moves(seq)
      min_seq_len = min(
        min_seq_len,
        shortest_seq(sub_t_seq, depth - 1, cache, graph)
      )

    total += min_seq_len

  cache[(key_str, depth)] = total
  return total


def part1(codes, num_grid, d_grid, repeat):
  total_complexity = 0

  collect_num_moves = {}
  all_nums = [x for sub in num_grid for x in sub]
  for i in all_nums:
    for j in all_nums:
      t = init_move(i, j, num_grid)
      collect_num_moves[(i, j)] = t

  collect_d_moves = {}
  all_ds = [x for sub in d_grid for x in sub]
  for i in all_ds:
    for j in all_ds:
      t = init_move(i, j, d_grid)
      collect_d_moves[(i, j)] = t

  cache = {}
  for code in codes:
    t_code = transform_moves(code, d=False)
    num_seqs = build_seq(t_code, collect_num_moves)

    min_seq = float("inf")

    for num_seq in num_seqs:
      t_seq = transform_moves(num_seq)
      min_seq = min(
        min_seq, shortest_seq(t_seq, repeat, cache, collect_d_moves)
      )

    total_complexity += min_seq * int(code[:-1])

  return total_complexity


# main

num_grid = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [-1, 0, 0.5]]
d_grid = [[-1, 0, 0.5], [-4, -3, -2]]
codes = []

with open("input21.txt", "r") as file:
  codes = file.read().split(sep)

sol1 = part1(codes, num_grid, d_grid, 2)
print("part 1:", sol1)

sol2 = -1
print("part 2:", sol2)
