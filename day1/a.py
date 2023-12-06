import re


def read_input():
    with open("input.txt") as f:
        content = f.read()

    return content.splitlines()


def main():
    lines = read_input()

    sum_ = 0
    for line in lines:
        digits = re.findall(r"\d", line)
        sum_ += int(digits[0] + digits[-1])
    print(sum_)


if __name__ == "__main__":
    main()
