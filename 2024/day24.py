from graphviz import Digraph


def vis(data):
  dot = Digraph()
  dot.attr(rankdir="LR", splines="polyline", nodesep="0.5", ranksep="1")

  levels = {}

  for p in data:
    c = ["green", "blue", "red"]["&|^".index(p[2])]

    for parent in p[0]:
      if parent not in levels:
        levels[parent] = "parent"
        dot.node(parent, style="filled", fillcolor="white")

    if p[1].startswith("z"):
      levels[p[1]] = "child"
      dot.node(p[1], style="filled", fillcolor="lightblue")
    else:
      dot.node(p[1], style="filled", fillcolor="lightgrey")

    dot.edge(p[0][0], p[1], color=c)
    dot.edge(p[0][1], p[1], color=c)

  dot.render("eqn_pairs", format="png")


def part1(d, eqns):
  while eqns:
    eqn = eqns.pop(0)
    try:
      d[eqn[1]] = eval(eqn[0])
    except KeyError:
      eqns.append(eqn)

  z_vals = [(k, v) for k, v in sorted(d.items(), reverse=True) if k.startswith("z")]
  z_vals_bin = "".join(str(x[1]) for x in z_vals)

  return int(z_vals_bin, 2)


def part2_failed(d, eqns):
  x_vals = [(k, v) for k, v in sorted(d.items(), reverse=True) if k.startswith("x")]
  x_vals_bin = "".join(str(x[1]) for x in x_vals)
  x_total = int(x_vals_bin, 2)

  y_vals = [(k, v) for k, v in sorted(d.items(), reverse=True) if k.startswith("y")]
  y_vals_bin = "".join(str(x[1]) for x in y_vals)
  y_total = int(y_vals_bin, 2)

  total = x_total + y_total
  total_bin = bin(total)[2:]

  actual = part1(d, eqns.copy())
  actual_bin = bin(actual)[2:]
  diff = [i for i in range(len(total_bin)) if total_bin[i] != actual_bin[i]]
  diff_strs = ["z" + str(x).zfill(2) for x in diff]
  diff_indices = [i for i, eqn in enumerate(eqns) if eqn[1] in diff_strs]

  # print(len(list(permutations([i for i, eqn in enumerate(eqns) if eqn[1] in diff_strs]))))

  # for p in permutations([i for i, eqn in enumerate(eqns) if eqn[1] in diff_strs]):
  #   temp_eqns = eqns.copy()
  #   for i, j in enumerate(p):
  #     temp_eqns[i], temp_eqns[j] = temp_eqns[j], temp_eqns[i]
  #   print(part1(d, temp_eqns))


def part2(eqn_pairs):
  d = {}
  for p in eqn_pairs:
    d[(p[0], p[2])] = p[1]

  prev_carry = "jtm"  # based on my input

  # starting check at 5 because everything before looks good
  for i in range(5, 45):
    x = "x" + str(i).zfill(2)
    y = "y" + str(i).zfill(2)

    pre_reg1 = "-1"
    pre_reg2 = "-1"

    if ((x, y), "^") in d:
      pre_reg1 = d[((x, y), "^")]
    elif ((y, x), "^") in d:
      pre_reg1 = d[((y, x), "^")]
    else:
      print("cond 1", i, ((x, y), "^"))
      break

    if ((x, y), "&") in d:
      pre_reg2 = d[((x, y), "&")]
    elif ((y, x), "&") in d:
      pre_reg2 = d[((y, x), "&")]
    else:
      print("cond 2", i, ((x, y), "&"))
      break

    reg1 = "-1"

    if ((pre_reg1, prev_carry), "^") in d:
      _ = d[((pre_reg1, prev_carry), "^")]
    elif ((prev_carry, pre_reg1), "^") in d:
      _ = d[((prev_carry, pre_reg1), "^")]
    else:
      print("cond 3", i, ((pre_reg1, prev_carry), "^"))
      break

    if ((pre_reg1, prev_carry), "&") in d:
      reg1 = d[((pre_reg1, prev_carry), "&")]
    elif ((prev_carry, pre_reg1), "&") in d:
      reg1 = d[((prev_carry, pre_reg1), "&")]
    else:
      print("cond 4", i, ((pre_reg1, prev_carry), "&"))
      break

    if ((reg1, pre_reg2), "|") in d:
      prev_carry = d[((reg1, pre_reg2), "|")]
    elif ((pre_reg2, reg1), "|") in d:
      prev_carry = d[((pre_reg2, reg1), "|")]
    else:
      print("cond 5", i)
      break


# main
sep = "\n"

d = {}
eqn_pairs = []
eqns = []

with open("input24.txt", "r") as file:
  parts = file.read().split(sep * 2)

  for line in parts[0].split(sep):
    part = line.split(": ")
    d[part[0]] = int(part[1])

  for line in parts[1].split(sep):
    l_parts = line.split(" -> ")
    rep = {
      "AND": "&",
      "OR": "|",
      "XOR": "^"
    }

    left = list(map(lambda x: rep.get(x, x), l_parts[0].split(" ")))
    eqn_pairs.append(((left[0], left[-1]), l_parts[1], left[1]))

    left[0] = "d[\"" + left[0] + "\"]"
    left[-1] = "d[\"" + left[-1] + "\"]"
    left = " ".join(left)

    right = l_parts[1]

    eqns.append((left, right))

# vis(eqn_pairs)

sol1 = part1(d, eqns.copy())
print("part 1:", sol1)

sol2 = part2(eqn_pairs.copy())
print("part 2:", sol2)
