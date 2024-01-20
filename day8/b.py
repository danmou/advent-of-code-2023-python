import re
from itertools import cycle

import z3


def read_input():
    with open("input.txt") as f:
        content = f.read().strip().splitlines()

    instructions = list(content[0])
    neighbors = {}
    starts = []

    for line in content[2:]:
        match = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
        neighbors[match.group(1)] = (match.group(2), match.group(3))
        if match.group(1).endswith("A"):
            starts.append(match.group(1))

    return instructions, neighbors, starts


def main():
    instructions, neighbors, starts = read_input()
    print(starts)
    cycles = {}
    end_indices = {}
    for start in starts:
        loc = start
        counter = 0
        end_indices[start] = []
        visited = set()
        visit_order = []
        for i, instruction in cycle(enumerate(instructions)):
            loc = neighbors[loc][0 if instruction == "L" else 1]
            counter += 1
            if (i, loc) in visited:
                # print(f"Cycle: {i}, {loc}")
                cycle_start = visit_order.index((i, loc))
                cycle_length = counter - cycle_start
                cycles[start] = cycle_start, cycle_length
                break
            if loc.endswith("Z"):
                # print(f"End: {i}, {loc}")
                end_indices[start].append(counter)
            visited.add((i, loc))
            visit_order.append((i, loc))
        print(start, cycles[start], end_indices[start])

    s = z3.Solver()
    k = z3.Int("k")
    for i, start in enumerate(starts[2:4]):
        cycle_start, cycle_length = cycles[start]
        end_index = end_indices[start][0]
        x = z3.Int(f"x{i}")
        print(f"{k} == {cycle_start} + {cycle_length} * {x} + {end_index}, {x} >= 0")
        s.add(k == cycle_start + cycle_length * x + end_index, x >= 0)

    print(s.check())
    m = s.model()
    print(m[k])


if __name__ == "__main__":
    main()
