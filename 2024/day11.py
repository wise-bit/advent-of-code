from collections import Counter
sep = "\n"  # separator

sol = 0
stones = []


def process_stones(stones, blinks):
  if blinks == 0:
    return stones

  added_stones = []

  for i in range(len(stones)):
    stone_str = str(stones[i])

    if stones[i] == 0:
      stones[i] = 1

    elif len(stone_str) % 2 == 0:
      stones[i] = int(stone_str[:len(stone_str) // 2])
      added_stones.append((i, int(stone_str[len(stone_str) // 2:])))

    else:
      stones[i] = stones[i] * 2024

  for stone_tup in added_stones:
    stones.insert(stone_tup[0] + 1, stone_tup[1])

  return process_stones(stones, blinks - 1)


def process_stones_iter(stones, blinks):
  stone_counts = Counter(stones)

  for i in range(blinks):
    # print(i)
    new_counts = Counter()

    for stone, count in stone_counts.items():
      stone_str = str(stone)

      if stone == 0:
        new_counts[1] += count

      elif len(stone_str) % 2 == 0:
        new_counts[int(stone_str[:len(stone_str) // 2])] += count
        new_counts[int(stone_str[len(stone_str) // 2:])] += count

      else:
        new_counts[stone * 2024] += count

    stone_counts = new_counts

  return sum(stone_counts.values())


with open("input11.txt", "r") as file:
  lines = file.read().split(sep)
  stones = list(map(int, lines[0].split()))

# sol = len(process_stones(stones, 25))
sol = process_stones_iter(stones, 75)

print(sol)
