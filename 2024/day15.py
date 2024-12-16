from time import sleep

sep = "\n"  # separator

g = []
moves = []

d = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def vis_g(g, bot):
  for r, line in enumerate(g):
    line_str = ""
    for c, ch in enumerate(line):
      if (r, c) == bot:
        line_str += "@"
      else:
        line_str += ch
    print(line_str)
  print()


def get_bot_pos(g):
  h, w = len(g), len(g[0])

  for r in range(h):
    for c in range(w):
      if g[r][c] == "@":
        bot = (r, c)
        g[r][c] = "."
        return bot


def move_bot_orig(g, moves, bot):
  for m in moves:
    new_pos = (bot[0] + d[m][0], bot[1] + d[m][1])
    if g[new_pos[0]][new_pos[1]] == "#":
      continue

    elif g[new_pos[0]][new_pos[1]] == "O":
      curr_pos = new_pos

      while g[curr_pos[0]][curr_pos[1]] == "O":
        next_pos = (curr_pos[0] + d[m][0], curr_pos[1] + d[m][1])
        if g[next_pos[0]][next_pos[1]] == "#":
          break

        curr_pos = next_pos

      if g[curr_pos[0]][curr_pos[1]] == ".":
        g[curr_pos[0]][curr_pos[1]] = "O"
        g[new_pos[0]][new_pos[1]] = "."

      else:
        continue

    bot = new_pos

  return g


def move_bot_trans(g, moves, bot):
  for m in moves:
    # vis_g(g, bot)
    # sleep(0.5)

    new_pos = (bot[0] + d[m][0], bot[1] + d[m][1])

    if g[new_pos[0]][new_pos[1]] == "#":
      continue

    elif g[new_pos[0]][new_pos[1]] in "[]":
      curr_pos = new_pos

      # horizontal
      if m in "><":
        while g[curr_pos[0]][curr_pos[1]] in "[]":
          next_pos = (curr_pos[0] + d[m][0], curr_pos[1] + d[m][1])
          if g[next_pos[0]][next_pos[1]] == "#":
            break

          curr_pos = next_pos

        if g[curr_pos[0]][curr_pos[1]] == ".":
          if m == "<":
            for i in range(curr_pos[1], new_pos[1]):
              g[bot[0]][i] = g[bot[0]][i + 1]
          else:
            for i in range(curr_pos[1], new_pos[1], -1):
              g[bot[0]][i] = g[bot[0]][i - 1]
          g[new_pos[0]][new_pos[1]] = "."

        else:
          continue

      # vertical
      else:
        curr_pos = new_pos
        q = [curr_pos]
        obs = {curr_pos}
        blocked = False

        if g[curr_pos[0]][curr_pos[1]] == "[":
          q.append((curr_pos[0], curr_pos[1] + 1))
          obs.add((curr_pos[0], curr_pos[1] + 1))
        else:
          q.append((curr_pos[0], curr_pos[1] - 1))
          obs.add((curr_pos[0], curr_pos[1] - 1))

        while len(q) > 0:
          curr_pos = q.pop(0)
          next_pos = (curr_pos[0] + d[m][0], curr_pos[1] + d[m][1])

          if g[next_pos[0]][next_pos[1]] == "#":
            blocked = True
            break

          new_obs, new_obs_side = None, None

          if g[next_pos[0]][next_pos[1]] == "[":
            new_obs = (next_pos[0], next_pos[1])
            new_obs_side = (next_pos[0], next_pos[1] + 1)

          elif g[next_pos[0]][next_pos[1]] == "]":
            new_obs = (next_pos[0], next_pos[1])
            new_obs_side = (next_pos[0], next_pos[1] - 1)

          # is new obs really new
          if new_obs and new_obs not in obs:
            q.append(new_obs)
            q.append(new_obs_side)
            obs.add(new_obs)
            obs.add(new_obs_side)

        if blocked:
          continue

        obs = sorted(list(obs))
        obs_new_positions = [(o[0] + d[m][0], o[1] + d[m][1]) for o in obs]
        for i in range(len(obs)):
          g[obs[i][0]][obs[i][1]] = "."

        left_obs = True
        for i in range(len(obs_new_positions)):
          g[obs_new_positions[i][0]][obs_new_positions[i][1]] = "]["[left_obs]
          left_obs = not left_obs

    bot = new_pos

  # vis_g(g, bot)
  return g


def box_coords_sum_orig(g):
  t = 0
  for y in range(len(g)):
    for x in range(len(g[0])):
      if g[y][x] == "O":
        t += y * 100 + x

  return t


def box_coords_sum_trans(g):
  t = 0
  for y in range(len(g)):
    for x in range(len(g[0])):
      if g[y][x] == "[":
        t += y * 100 + x

  return t


def transform_grid(g):
  new_g = []

  for row in g:
    new_g.append(
      list(
        "".join(row)
        .replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
      )
    )

  return new_g


def part1(g):
  g_copy = [x[:] for x in g]
  bot = get_bot_pos(g_copy)
  g_moved = move_bot_orig(g_copy, moves, bot)

  return box_coords_sum_orig(g_moved)


def part2(g):
  g_copy = [x[:] for x in g]
  g2 = transform_grid(g_copy)
  bot = get_bot_pos(g2)
  g_moved = move_bot_trans(g2, moves, bot)

  return box_coords_sum_trans(g_moved)


# main

with open("input15.txt", "r") as file:
  parts = file.read().split("\n\n")

  for line in parts[0].split(sep):
    g.append(list(line))

  moves = list("".join(parts[1].split(sep)))

sol1 = part1(g)
print("part 1:", sol1)

sol2 = part2(g)
print("part 2:", sol2)
