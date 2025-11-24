import math


sep = "\n"  # separator
c = 0  # counter

left = []
right = []

# Part 1

with open("input02.txt", "r") as file:
  lines = file.read().split(sep)
  games = []

  max_counts = {
    "red": 12,
    "green": 13,
    "blue": 14,
  }

  good_games = 0

  for _l in lines:
    # entries = line.split()
    id_src, l = _l.split(": ")
    id = int(id_src.split()[1])

    game_raw = l.split("; ")
    game = [g.split(", ") for g in game_raw]

    good = True

    for rounds in game:
      counts = {}

      for r in rounds:
        picks = r.split()

        if picks[1] not in counts:
          counts[picks[1]] = int(picks[0])
        else:
          counts[picks[1]] += int(picks[0])

      for color in counts.keys():
        if counts[color] > max_counts[color]:
          # print(color, counts[color], max_counts[color])
          good = False
          break

    if good:
      # print(id)
      good_games += id  # id / 1

    # print(counts)

  print(good_games)


print("\n=====\n")


# Part 2

with open("input02.txt", "r") as file:
  lines = file.read().split(sep)
  total_power = 0

  for _l in lines:
    id_src, l = _l.split(": ")
    id = int(id_src.split()[1])

    game = [g.split(", ") for g in l.split("; ")]

    max_counts = {
      "red": 0,
      "green": 0,
      "blue": 0,
    }

    for rounds in game:
      counts = {}

      for r in rounds:
        picks = r.split()

        if picks[1] not in counts:
          counts[picks[1]] = int(picks[0])
        else:
          counts[picks[1]] = max(counts[picks[1]], int(picks[0]))

      for color in counts.keys():
        if counts[color] > max_counts[color]:
          max_counts[color] = counts[color]

    power = math.prod(max_counts.values())
    total_power += power

  print(total_power)
