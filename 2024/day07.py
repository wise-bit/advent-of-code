sep = "\n"  # separator

sol_1 = 0
sol_2 = 0


def concatenate(a, b):
  return int(str(a) + str(b))


def possible(final, nums, i, total, do_concat=False):
  if i == len(nums):
    return total == final

  if possible(final, nums, i + 1, total + nums[i], do_concat):
    return True

  if possible(final, nums, i + 1, total * nums[i], do_concat):
    return True

  if do_concat and possible(final, nums, i + 1, concatenate(total, nums[i]), do_concat):
    return True

  return False


with open("input07.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    parts = line.split(": ")
    final = int(parts[0])
    nums = list(map(int, parts[1].split()))

    if possible(final, nums, 0, 0):
      sol_1 += final

    if possible(final, nums, 0, 0, True):
      sol_2 += final

print(sol_1)
print(sol_2)
