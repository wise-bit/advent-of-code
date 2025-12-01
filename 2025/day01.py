sep = "\n"


def fn():
  pass


def part1(r):
  pos = 50
  # print(r)

  cnt = 0

  for c in r:
    mv = int(c[1:])
    if c.startswith("R"):
      pos += mv
    else:
      pos -= mv
    
    pos %= 100

    if pos == 0:
      cnt += 1

  
  print(cnt)



def part2(r):
  pos = 50
  # print(r)

  cnt = 0

  for c in r:
    pos_prev = pos
    mv = int(c[1:])
    if mv > 100:
      cnt += mv // 100
      mv %= 100
    if c.startswith("R"):
      pos += mv
    else:
      pos -= mv

    if (
      pos == 0 or 
      pos == 100 or 
      (pos_prev < 0 and pos > 0) or (pos_prev > 0 and pos < 0) or 
      (pos_prev < 100 and pos > 100) or (pos_prev > 100 and pos < 100)
    ):
      # print(pos_prev, pos)
      cnt += 1
    
    pos %= 100
    # print(pos)

  print(cnt)


# main

a = []

with open("input01.txt", "r") as file:
  lines = file.read().split(sep)

  for line in lines:
    pass


sol1 = part1(lines)
print("part 1:", sol1)

sol2 = part2(lines)
print("part 2:", sol2)
