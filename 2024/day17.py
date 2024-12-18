sep = "\n"

sol1 = 0
sol2 = 0


def run(a, b, c, program):
  def get_combo(x):
    if x <= 3:
      return x
    if x == 4:
      return reg_a
    if x == 5:
      return reg_b
    if x == 6:
      return reg_c
    if x == 7:
      return

  reg_a, reg_b, reg_c = a, b, c
  outputs = []
  ins = 0

  while ins < len(program) - 1:
    op = program[ins]
    lit = program[ins + 1]
    combo = get_combo(lit)

    if op == 0:
      reg_a = reg_a // (2 ** combo)
      ins += 2

    elif op == 1:
      reg_b = reg_b ^ lit
      ins += 2

    elif op == 2:
      reg_b = combo % 8
      ins += 2

    elif op == 3:
      if reg_a == 0:
        ins += 2
        continue
      else:
        ins = lit

    elif op == 4:
      reg_b = reg_b ^ reg_c
      ins += 2

    # only code that outputs
    elif op == 5:
      outputs.append(combo % 8)
      ins += 2

    elif op == 6:
      reg_b = reg_a // (2 ** combo)
      ins += 2

    elif op == 7:
      reg_c = reg_a // (2 ** combo)
      ins += 2

  return ",".join(str(o) for o in outputs)


def search_a_brute(b, c, program):
  prog_str = ",".join(str(p) for p in program)
  for i in range(1174410):
    out = run(i, b, c, program)
    if out == prog_str:
      return i


def search_a(program):
  a_values = [0]
  xors = [program[3], program[7]]  # fixed for my input

  # check in batch starting from back 
  for val in program[::-1]:
    regs_a = []

    for temp_a in a_values:
      # print(regs_a)

      start = temp_a * 8
      end = temp_a * 8 + 8

      # inverted ((a % 8) ^ 3) ^ (a >> ((a % 8) ^ 3))
      # derived from my input

      for check_val in range(start, end):
        curr_b = check_val % 8
        curr_c = check_val // (2 ** (curr_b ^ 3))

        if (val ^ curr_c ^ xors[0] ^ xors[1]) % 8 == check_val % 8:
          regs_a.append((temp_a * 8) + curr_b)

    a_values = regs_a

  return a_values


# main

inp_a = inp_b = inp_c = 0
inp_program = []

with open("input17.txt", "r") as file:
  lines = file.read().split(sep)

  inp_a = int(lines[0].split(": ")[1])
  inp_b = int(lines[1].split(": ")[1])
  inp_c = int(lines[2].split(": ")[1])
  inp_program = list(map(int, (lines[4].split(": ")[1].split(","))))

sol1 = run(inp_a, inp_b, inp_c, inp_program)
print("part 1:", sol1)

sol2 = search_a(inp_program)[0]
print("part 2:", sol2)
