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

    sum_ = 0
    for winning, actual in cards:
        num_winning = len(winning & actual)
        if num_winning:
            sum_ += 2 ** (num_winning - 1)

    print(sum_)


if __name__ == "__main__":
    main()
