import re


sep = "\n"


def fn():
  pass


def mult_list(l):
  result = 1
  for x in l:
    result *= x
  return result


def normalize_list(l):
  max_l = max([len(_l) for _l in l])
  padded_str_l = [(str(x) + "x" * max(0, max_l - len(str(x)))) for x in l]
  # print(padded_str_l)

  return padded_str_l


def str_splitter(s, d="x"):
  res = []
  acc = ""
  i = 0
  n = len(s)
  
  while i < n:
    if s[i] == d:
      j = i
      while j < n and s[j] == d:
        j += 1
      run_len = j - i
      
      if run_len == 1:
        if acc:
          acc += d
          res.append(acc)
          acc = ""
        i += 1

      else:
        acc += s[i:j]
        i = j

    else:
      acc += s[i]
      i += 1

  if acc:
    res.append(acc)
  
  return res


def split_lines_new(lines):
  l2 = []

  max_len = max(len(l) for l in lines)
  padded = [l.ljust(max_len) for l in lines]
  transp = [list(col) for col in zip(*padded)]

  cols = []
  start = 0

  for i, col in enumerate(transp):
    if all(c == ' ' or c == 'x' for c in col):
      if start != i:
        cols.append((start, i))

      start = i + 1

  cols.append((start, len(transp)))
  # print(cols)

  res = []
  for l in lines:
    row = []
    for s, e in cols:
      row.append(l[s:e].strip())

    res.append(row)

  for r in res:
    l2.append(r)
  
  return l2


def clean_xs(l):
  l2 = []
  # print(l)

  for i in range(len(l)):
    if all([s.startswith("x") for s in l[i]]):
      max_l = max([len(s) for s in l[i]])
      l2.append([s[len(s) - max_l + 1:] for s in l[i]])
    else:
      l2.append(l[i])

  return l2


# ---


def part1(num_sets, last_line):
  sol = 0
  rs = len(num_sets[0])

  for r in range(rs):
    nums = [num_set[r] for num_set in num_sets]
    # print(nums)

    if last_line[r] == "+":
      sol += sum(nums)
    else:
      sol += mult_list(nums)

  return sol


def part2(num_sets, last_line):
  sol = 0

  transposed = [list(col) for col in zip(*num_sets)]
  # print(transposed)

  cleaned_sets = clean_xs(transposed)
  # print(cleaned_sets)

  # rs = len(cleaned_sets[0])

  r = 0

  for nums in cleaned_sets:
    # nums = [num_set[r] for num_set in cleaned_sets]
    nums_str = normalize_list(nums)

    # print(nums_str)

    nums_strs = []
    for s in nums_str:
      nums_strs.append(list(s))
    nums_strs = list(zip(*nums_str))

    # print(nums)
    # print(nums_strs)
    # print("===")

    joined_nums = []
    for a in nums_strs:
      # joined_nums.append(int(a.replace("x", "0")))
      joined_nums.append(int("".join([x for x in a if x != "x"])))

    # print(joined_nums)

    # nums_str_split = [list(s) for s in nums_str]
    # print(nums_str_split)
  
    if last_line[r] == "+":
      sol += sum(joined_nums)
    else:
      sol += mult_list(joined_nums)
    
    r += 1
  
  return sol


if __name__ == "__main__":
  num_sets = []
  num_sets_2 = []
  last_line = []

  with open("input06.txt", "r") as file:
    lines = file.read().split(sep)
    num_sets_raw = lines[:-1]

    # chunk_count = len(lines[0].split("x"))
    num_sets_raw_x = [s.replace(" ", "x") for s in num_sets_raw]
    # print(num_sets_raw_x)

    chunks = split_lines_new(num_sets_raw_x)
    # print(chunks)

    num_sets_2 = chunks

    for s in num_sets_raw:
      num_sets.append(list(map(int, s.split())))

      # s = s.replace(" ", "")
      # raw_s_list = [s[i:i+3] for i in range(0, len(s), 4)]

      # sx = s.replace(" ", "x")
      # print(str_splitter(sx))

      # pattern = r'xx*\d+|x\d+|\d+x?|\d+'
      # chunks = re.findall(pattern, s.replace(" ", "x"))

      # chunks = str_splitter(sx)
      # num_sets_2.append(chunks)

      # chunk_count = len(s.split())
      # chunks = split_lines_fixed_width(lines, chunk_count)

      # print(chunks)

    last_line = lines[-1].split()

    # print(num_sets, last_line)

  sol1 = part1(num_sets, last_line)
  print("part 1:", sol1)

  sol2 = part2(num_sets_2, last_line)
  print("part 2:", sol2)

  # print(str_splitter("921x283x29xx93"))
