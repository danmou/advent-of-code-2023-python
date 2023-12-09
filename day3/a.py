import re


def read_input():
    with open("input.txt") as f:
        content = f.read()

    lines = []
    for line in content.strip().splitlines():
        if not lines:
            lines.append("." * (len(line) + 2))
        lines.append("." + line + ".")
    lines.append("." * (len(line) + 2))
    return lines


def main():
    lines = read_input()

    sum_ = 0
    for row in range(1, len(lines) - 1):
        for match in re.finditer(r"\d+", lines[row]):
            # print(match.group())
            for x in range(match.start() - 1, match.end() + 1):
                for y in range(row - 1, row + 2):
                    char = lines[y][x]
                    # print(f"{x}, {y}: {char}")
                    if char != "." and not char.isdigit():
                        sum_ += int(match.group())
                        # print("yes")
                        break
                else:
                    continue
                break

    print(sum_)


if __name__ == "__main__":
    main()
