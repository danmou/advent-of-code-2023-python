import re


def read_input():
    with open("input.txt") as f:
        content = f.read()

    games = []
    for line in content.splitlines():
        sets = []
        for set in line.split(": ")[1].split(";"):
            sets.append({b: int(a) for a, b in [x.split() for x in set.split(", ")]})
        games.append(sets)
    return games


def main():
    games = read_input()

    sum_ = 0
    for i, game in enumerate(games):
        min_count = {}
        for set in game:
            for color, count in set.items():
                min_count[color] = max(min_count.get(color, 0), count)
        power = min_count.get("red", 0) * min_count.get("green", 0) * min_count.get("blue", 0)
        sum_ += power
    print(sum_)


if __name__ == "__main__":
    main()
