
def read_input():
    with open("input.txt") as f:
        content = f.read()

    time, record = [int("".join(line.split()[1:])) for line in content.strip().split("\n")]

    return time, record


def main():
    time, record = read_input()

    print(f"{time=}, {record=}")
    ways = 0
    for hold_time in range(1, time):
        if hold_time % 1000 == 0:
            print(hold_time)
        distance = hold_time * (time - hold_time)
        if distance > record:
            ways += 1
    print(f"{ways=}")


if __name__ == "__main__":
    main()
