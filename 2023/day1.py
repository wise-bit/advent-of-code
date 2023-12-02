sep = "\n"  # separator
c = 0  # counter

with open("input1.txt", "r") as file:
    d = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    s = 0
    lines = file.read().split(sep)
    for line in lines:
        l = line
        mod_l = ""
        index = 0

        while index < len(l):
            for old_str, new_str in d.items():
                if len(l) - index >= len(old_str) and l[index:index+len(old_str)] == old_str:
                    mod_l += new_str
                    index += len(old_str) - 1

                elif l[index].isdigit():
                    mod_l += l[index]
                    index += 1

                if index >= len(l):
                    break

            index += 1

        if len(mod_l) > 0:
            s += int(mod_l[0] + mod_l[-1])

    print(s)
