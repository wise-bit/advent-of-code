sep = "\n"  # separator
total = 0  # total

left = []
right = []

with open("input03.txt", "r") as file:
  line = file.read()

  # print(line)

  i = 0
  do = True

  while i < len(line):
    if line[i:i + 4] == "do()":
      do = True
      i += 4
      continue

    if line[i:i + 7] == "don't()":
      do = False
      i += 7
      continue

    if line[i:i + 4] == "mul(":
      if do:
        i += 4
        s = i

        while i < len(line) and line[i].isdigit():
          i += 1
        if i == s or line[i] != ',' or i >= len(line):
          continue

        num1 = int(line[s:i])
        i += 1

        s = i
        while i < len(line) and line[i].isdigit():
          i += 1
        if i == s or line[i] != ')' or i >= len(line):
          continue

        num2 = int(line[s:i])
        total += num1 * num2

        i += 1

      else:
        i += 4
        while i < len(line) and line[i] != ')':
          i += 1

        i += 1

    else:
      i += 1

print(total)
