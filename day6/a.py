
def read_input():
    with open("input.txt") as f:
        content = f.read()

    times, distances = [[int(x) for x in line.split()[1:]] for line in content.strip().split("\n")]

    return times, distances


def main():
    times, distances = read_input()

    ways_prod = 1
    for time, record in zip(times, distances):
        print(f"{time=}, {record=}")
        ways = 0
        for hold_time in range(1, time):
            distance = hold_time * (time - hold_time)
            if distance > record:
                ways += 1
        print(f"{ways=}")
        ways_prod *= ways
    print(f"{ways_prod=}")


if __name__ == "__main__":
    main()
