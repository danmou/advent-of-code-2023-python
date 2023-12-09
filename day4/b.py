import re


def read_input():
    with open("input.txt") as f:
        content = f.read()

    cards = []
    for line in content.splitlines():
        cards.append(
            [
                {int(x.strip()) for x in part.strip().split()}
                for part in line.split(":")[1].split("|")
            ]
        )

    return cards


def main():
    cards = read_input()

    counts = []
    for winning, actual in cards:
        num_winning = len(winning & actual)
        counts.append(num_winning)

    print(counts)

    values = [1] * len(counts)
    for i in range(len(counts) - 1, -1, -1):
        count = counts[i]
        for j in range(i, i + count):
            values[i] += values[j + 1]

    print(values)
    print(sum(values))


if __name__ == "__main__":
    main()
