import re


def part1(inputs: list[str]) -> int:
    pattern = re.compile(r"\d")
    return sum(
        [int(f"{pattern.findall(i)[0]}{pattern.findall(i)[-1]}") for i in inputs]
    )


def part2(inputs: list[str]) -> int:
    repl = {
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

    replace_pattern = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine))")

    replaced_inputs = [
        replace_pattern.sub(lambda x: repl.get(x.group(1), ""), i) for i in inputs
    ]

    return part1(replaced_inputs)


if __name__ == "__main__":
    inputs = [line.rstrip("\n") for line in open("input1.txt")]
    print(part1(inputs))
    print(part2(inputs))
