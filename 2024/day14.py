from functools import reduce
import os
from PIL import Image
from tempfile import mkdtemp

sep = "\n"  # separator

sol = 0
bots = []


def visualize(dims, bots_new_positions):
  width, height = dims
  floor = [['.' for _ in range(width)] for _ in range(height)]

  for pos in bots_new_positions:
    x, y = pos
    floor[y][x] = 'X'

  vis = ""
  for row in floor:
    vis += ''.join(row) + "\n"

  print(vis)


def move_bots(dims, bots, n):
  width, height = dims
  new_positions = []

  for robot in bots:
    x, y, dx, dy = robot

    new_x = (x + dx * n) % width
    new_y = (y + dy * n) % height

    new_positions.append([new_x, new_y])

  return new_positions


def count_bots(dims, bots_new_positions):
  width, height = dims

  mid_x = width // 2
  mid_y = height // 2

  quad_cnt = {'0': 0, '1': 0, '2': 0, '3': 0}

  for pos in bots_new_positions:
    x, y = pos

    if x == mid_x or y == mid_y:
      continue

    if x < mid_x and y < mid_y:
      quad_cnt['0'] += 1
    elif x >= mid_x and y < mid_y:
      quad_cnt['1'] += 1
    elif x < mid_x and y >= mid_y:
      quad_cnt['2'] += 1
    elif x >= mid_x and y >= mid_y:
      quad_cnt['3'] += 1

  prod = reduce(lambda x, y: x * y, quad_cnt.values())
  return prod


def save_art(dims, bots_pos, time_step, temp_folder):
  width, height = dims

  floor = [['.' for _ in range(width)] for _ in range(height)]
  for pos in bots_pos:
    x, y = pos
    floor[y][x] = 'X'

  vis = ""
  for row in floor:
    vis += ''.join(row) + "\n"

  image = Image.new('1', (width, height), 1)
  pixels = image.load()

  for y in range(height):
    for x in range(width):
      pixels[x, y] = 0 if floor[y][x] == 'X' else 1

  image_filename = os.path.join(temp_folder, f"{time_step}.png")
  image.save(image_filename)


def visualize_save(dims, bots, time, temp_folder):
  for t in range(1, time + 1):
    moved_bots = move_bots(dims, bots, t)
    save_art(dims, moved_bots, t, temp_folder)


with open("input14.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    parts = line.split(" ")

    pos = list(map(int, parts[0].split("=")[1].split(",")))
    mov = list(map(int, parts[1].split("=")[1].split(",")))

    bots.append(pos + mov)


# main

dims = [101, 103]
time = 100

moved_bots = move_bots(dims, bots, time)
sol = count_bots(dims, moved_bots)
print(sol)

#
# manual inspection of bots

# time_steps = 100
# temp_folder = mkdtemp(dir="./tmp/")
# print(temp_folder)
# visualize_save(dims, bots, time_steps, temp_folder)

test_time = 10000
s = []
for t in range(1, test_time + 1):
  moved_bots = move_bots(dims, bots, t)
  if len(set(tuple(x) for x in moved_bots)) == len([tuple(x) for x in moved_bots]):
    s.append(t)

print(f"Easter egg: {s}")
# visualize(dims, move_bots(dims, bots, s[0]))
