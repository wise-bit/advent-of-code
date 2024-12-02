sep = "\n"  # separator
c = 0  # counter


def is_safe_1(ls):
  ds = [ls[i + 1] - ls[i] for i in range(len(ls) - 1)]

  if not all(-3 <= d <= 3 and d != 0 for d in ds):
    return False
  if all(d > 0 for d in ds) or all(d < 0 for d in ds):
    return True

  return False


def is_safe_2(ls):
  if is_safe_1(ls):
    return True

  for i in range(len(ls)):
    modded = ls[:i] + ls[i + 1:]
    if is_safe_1(modded):
      return True

  return False


safes = 0

with open("input02.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    nums = list(map(int, line.split()))

    if is_safe_2(nums):
      safes += 1

print(safes)
