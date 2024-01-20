import re
from itertools import cycle


def read_input():
    with open("input.txt") as f:
        content = f.read().strip().splitlines()

    instructions = list(content[0])
    neighbors = {}

    for line in content[2:]:
        match = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
        neighbors[match.group(1)] = (match.group(2), match.group(3))

    return instructions, neighbors


def main():
    instructions, neighbors = read_input()
    loc = "AAA"
    counter = 0
    for instruction in cycle(instructions):
        if instruction == "L":
            loc = neighbors[loc][0]
        elif instruction == "R":
            loc = neighbors[loc][1]
        else:
            raise ValueError(f"Invalid instruction {instruction}")
        counter += 1
        if loc == "ZZZ":
            break
    print(counter)


if __name__ == "__main__":
    main()
