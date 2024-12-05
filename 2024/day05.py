sep = "\n"  # separator

rules = []
updates = []
result = 0

fix_ordering = True  # part 2 enable

with open("input05.txt", "r") as file:
  lines = file.read().split(sep)
  read_i = 0

  line = lines[0]
  while line != "":
    ps = line.split("|")
    rules.append((int(ps[0]), int(ps[1])))
    read_i += 1
    line = lines[read_i]

  read_i += 1
  for i in range(read_i, len(lines)):
    updates.append(lines[i].split(","))

updates = [list(map(int, update)) for update in updates]

for update in updates:
  correct = True

  change_made = True
  while change_made:
    change_made = False

    for rule in rules:
      not_exist = False
      try:
        a = update.index(rule[0])
        b = update.index(rule[1])

        if a > b:
          correct = False
          if not fix_ordering:
            break

          change_made = True
          cc = update[a]
          update[a] = update[b]
          update[b] = cc

      except:
        not_exist = True

      if not_exist:
        continue

  if (not correct and fix_ordering) or (correct and not fix_ordering):
    result += update[len(update) // 2]

print(result)
