sep = "\n"


def dfs(d, node, end, memo, active, word1 = "", word2 = "", seen_word1 = False, seen_word2 = False):
  if node == end:
    return 1 if seen_word1 and seen_word2 else 0

  state = (node, seen_word1, seen_word2)

  if state in memo:
    return memo[state]

  if node in active:
    return 0

  _seen_word1 = seen_word1 or node == word1
  _seen_word2 = seen_word2 or node == word2

  active.add(node)
  total = 0

  for n in d.get(node, []):
    total += dfs(d, n, end, memo, active, word1, word2, _seen_word1, _seen_word2)

  active.remove(node)
  memo[state] = total

  return total


# ---


def part1(d):
  return dfs(d, "you", "out", dict(), set(), seen_word1=True, seen_word2=True)


def part2(d):
  return dfs(d, "svr", "out", dict(), set(), "dac", "fft")


if __name__ == "__main__":
  d = dict()

  with open("input11.txt", "r") as file:
    lines = file.read().split(sep)

    for line in lines:
      inp, out_raw = line.split(": ")
      out = out_raw.split()
      d[inp] = out

  sol1 = part1(d)
  print("part 1:", sol1)

  sol2 = part2(d)
  print("part 2:", sol2)
