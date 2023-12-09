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
        for set in game:
            # 12 red cubes, 13 green cubes, and 14 blue
            if set.get("red", 0) > 12 or set.get("green", 0) > 13 or set.get("blue", 0) > 14:
                break
        else:
            sum_ += i + 1
    print(sum_)


if __name__ == "__main__":
    main()
