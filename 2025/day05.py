sep = "\n"


def fn():
  pass


# ---


def part1(id_ranges, ids):
  sol = 0
  fresh = []

  for s_id in ids:
    id = int(s_id)

    fresh = False

    for id_range in id_ranges:
      id_start_end = id_range.split("-")

      start = int(id_start_end[0])
      end = int(id_start_end[1])

      if start <= id <= end:
        fresh = True
        break
    
    if fresh:
      sol += 1

  return sol


def part2(id_ranges):
  sol = 0
  id_ranges_int = []

  for id_range in id_ranges:
    id_start_end = id_range.split("-")
    start = int(id_start_end[0])
    end = int(id_start_end[1])

    id_ranges_int.append((start, end))

  id_ranges_int.sort()
  # print(range_ints[0])

  merged_rs = [list(id_ranges_int[0])]
  # print(merged_rs)

  for start, end in id_ranges_int[1:]:
    if start > merged_rs[-1][1] + 1:
      merged_rs.append([start, end])

    elif end > merged_rs[-1][1]:
      merged_rs[-1][1] = end

  # print(merged_rs)

  for start, end in merged_rs:
    sol += end - start + 1

  return sol


if __name__ == "__main__":
  id_ranges = []
  ids = []

  with open("input05.txt", "r") as file:
    line_sets = file.read().split(sep * 2)

    id_ranges = line_sets[0].split(sep)
    ids = line_sets[1].split(sep)

    # print(id_ranges, ids)

  sol1 = part1(id_ranges, ids)
  print("part 1:", sol1)

  sol2 = part2(id_ranges)
  print("part 2:", sol2)
