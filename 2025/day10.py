# from functools import cache
import pulp


sep = "\n"


def parse_tuple(s):
  return tuple(map(int, s[1:-1].split(',')))


def check_state(curr, goal):
  for i in range(len(curr)):
    if curr[i] != goal[i]:
      return False

  return True


def mask(bits):
  m = 0
  for i, b in enumerate(bits):
    if b:
      m |= (1 << i)

  return m


# def mag_mask(levels):
#   m = 0
#   for i, l in enumerate(levels):
#     m |= (l << i)

#   return m


def apply_toggle_ints(state, tog):
  new_state = list(state)
  for i in tog:
    new_state[i] += 1

  return tuple(new_state)


def encode(levels, slot_size):
  m = 0
  for i, l in enumerate(levels):
    m |= (l << (i * slot_size))

  return m


def decode(mask, slots, slot_size):
  vals = []
  for i in range(slots):
    shift = i * slot_size
    vals.append((mask >> shift) & ((1 << slot_size) - 1))

  return vals


# def apply_toggle(state, tog, n_slots, slot_size):
#   new_state = 0


# ---


def part1(machines):
  sol = 0

  for m in machines:
    goal = m[0]
    wiring = m[1]

    # state = [False] * len(goal)
    b_state = 0
    b_goal = mask(goal)

    # print(b_state, b_goal)

    b_wirings = []
    for w in wiring:
      m = 0
      for i in w:
        m |= (1 << i)
      b_wirings.append(m)

    # print(b_wirings)

    # bfs
    q = [(b_state, 0)]
    head = 0

    seen = {b_state}
    shortest_dist = -1

    while head < len(q):
      curr, dist = q[head]
      head += 1

      if curr == b_goal:
        shortest_dist = dist
        break

      for w in b_wirings:
        next_state = curr ^ w
        if next_state not in seen:
          seen.add(next_state)
          q.append((next_state, dist + 1))

    # print(goal)
    # print(wiring)
    # print(shortest_dist)

    sol += shortest_dist

  return sol


def part2(machines):
  sol = 0

  for i, m in enumerate(machines):
    # print(i)
    wirings = m[1]
    joltage = m[2]

    prob = pulp.LpProblem(f"M{i}", pulp.LpMinimize)
    xs = []
    for i in range(len(wirings)):
      xs.append(pulp.LpVariable(f"x_{i}", lowBound=0, cat=pulp.LpInteger))

    for slot in range(len(joltage)):
      xs_sub = []
      for i in range(len(wirings)):
        xs_sub.append(xs[i] if slot in wirings[i] else 0)

      prob += pulp.lpSum(xs_sub) == joltage[slot]

    prob += pulp.lpSum(xs)
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    sol += sum(int(var.value()) for var in xs)

  return sol


if __name__ == "__main__":
  a = []
  machines = []

  with open("input10.txt", "r") as file:
    lines = file.read().split(sep)

    for line in lines:
      goal_str, rest_str = line.split("] ")
      wiring_str, joltage_str = rest_str.split(" {")
      goal_str = goal_str[1:]
      wiring_substrs = wiring_str.split(" ")
      joltage_str = joltage_str[:-1]

      goal = [True if x == "#" else False for x in goal_str]
      wiring = [parse_tuple(s) for s in wiring_substrs]
      joltage = list(map(int, joltage_str.split(",")))

      machines.append([goal, wiring, joltage])

      # print(goal)
      # print(wiring)
      # print(joltage)

  sol1 = part1(machines)
  print("part 1:", sol1)

  sol2 = part2(machines)
  print("part 2:", sol2)
