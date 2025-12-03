sep = "\n"


def best_two(bank):
  batteries = list(map(int, bank))
  l = len(batteries)

  m = -1
  x, y = 0, 0

  for i in range(l):
    for j in range(i+1, l):
      _x, _y = batteries[i], batteries[j]
      s = _x * 10 + _y

      if s > m:
        m = s
        x, y = i, j

  return (x, y)


def best_n_batteries(bank, n=12):
  batteries = list(map(int, bank))
  l = len(batteries)

  picked = []
  extra = l - n

  for x in batteries:
    while (
      extra > 0 and 
      (len(picked) > 0 and picked[-1] < x)
    ):
      # print(picked)
      picked.pop()
      extra -= 1

    picked.append(x)

  picked = picked[:n]
  # print(picked)

  return picked


# ---


def part1(a):
  # print(a)
  sol = 0

  for bank in a:
    x, y = best_two(bank)

    # print(x, y)
    # l = 0
    # r = 1
    # for i in range(2, len(bank)):
    #   if bank[r] > bank[l] and i < len(bank) - 1:
    #     l = r
    #     r = i + 1
    #   elif bank[i] > bank[r]:
    #     r = i
    # print(l, r)

    sol += bank[x] * 10 + bank[y]

  return sol
  

def part2():
  sol = 0

  for bank in a:
    num = int("".join(str(x) for x in best_n_batteries(bank)))
    sol += num

  return sol


if __name__ == "__main__":
  a = []

  with open("input03.txt", "r") as file:
    lines = file.read().split(sep)

    for line in lines:
      a.append(list(map(int, list(line))))

  sol1 = part1(a)
  print("part 1:", sol1)

  sol2 = part2()
  print("part 2:", sol2)
