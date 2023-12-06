import re


def read_input():
    with open("input.txt") as f:
        content = f.read()

    return content.splitlines()


def main():
    lines = read_input()

    sum_ = 0
    numbers = {
        "zero": "0",
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
    for line in lines:
        print(line)
        matches = []
        for number in numbers.keys():
            matches += list(re.finditer(number, line))
        matches += list(re.finditer(r"\d", line))
        matches.sort(key=lambda x: x.start())
        first = matches[0].group()
        first = numbers[first] if first in numbers else first
        matches.sort(key=lambda x: x.end())
        last = matches[-1].group()
        last = numbers[last] if last in numbers else last
        sum_ += int(first + last)
    print(sum_)


if __name__ == "__main__":
    main()
