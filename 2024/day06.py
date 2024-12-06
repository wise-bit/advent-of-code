sep = "\n"  # separator


def sim_guard(m, start_pos, start_dir):
  dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
  turns = ['^', '>', 'v', '<']

  x, y = start_pos
  curr_dir = start_dir

  r, c = len(m), len(m[0])
  while 0 <= x < r and 0 <= y < c:
    if m[x][y] == '.':
      m[x][y] = '*'

    dx, dy = dirs[curr_dir]
    nx, ny = x + dx, y + dy

    if not (0 <= nx < r and 0 <= ny < c):
      break
    elif m[nx][ny] == '#':
      curr_dir = turns[(turns.index(curr_dir) + 1) % 4]
    else:
      x, y = nx, ny

  return m


def does_loop(m_cpy, x, y, curr_dir):
  dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
  turns = ['^', '>', 'v', '<']

  visited = set()
  while 0 <= x < len(m_cpy) and 0 <= y < len(m_cpy[0]):
    s = (x, y, curr_dir)
    if s in visited:
      return True
    visited.add(s)

    dx, dy = dirs[curr_dir]
    nx, ny = x + dx, y + dy

    if not (0 <= nx < len(m_cpy) and 0 <= ny < len(m_cpy[0])):
      break
    elif m_cpy[nx][ny] == '#':
      curr_dir = turns[(turns.index(curr_dir) + 1) % 4]
    else:
      x, y = nx, ny
  return False


def calc_obstacles(m, start_pos, start_dir):
  obs_cnt = 0

  r, c = len(m), len(m[0])
  obs = []
  for i in range(r):
    for j in range(c):
      if m[i][j] == '.':
        m[i][j] = '#'
        if does_loop(m, start_pos[0], start_pos[1], start_dir):
          obs.append((i, j))
          obs_cnt += 1
        m[i][j] = '.'

  for i, j in obs:
    m[i][j] = 'O'

  # print("\n".join("".join(l) for l in m) + "\n")
  return obs_cnt


with open("input06.txt", "r") as file:
  lines = file.read().split(sep)

  m = []
  start_pos = (-1, -1)
  start_dir = ""
  x = -1
  for line in lines:
    x += 1
    temp = []
    y = -1
    for c in line:
      y += 1
      if c in "<^>v":
        start_pos = (x, y)
        start_dir = c
        temp.append(".")
      else:
        temp.append(c)
    m.append(temp)

# print("\n".join("".join(l) for l in traverse) + "\n")

# part 1
# result = (
#   "".join(
#     "".join(l) for l in sim_guard(m, start_pos, start_dir)
#   ).count("*")
# )

# part 2
result = calc_obstacles(m, start_pos, start_dir)

print(result)
