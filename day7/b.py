from collections import Counter

CARDS = list("J23456789TQKA")


def read_input():
    with open("input.txt") as f:
        content = f.read().strip().splitlines()

    hands = []
    for line in content:
        cards, bid = line.split()
        cards = [CARDS.index(card) for card in cards]
        bid = int(bid)
        counts = Counter(cards)
        num_jokers = counts.pop(0, 0)
        if counts:
            highest = max(counts.items(), key=lambda x: x[1])[0]
        else:
            highest = 0
        counts[highest] += num_jokers
        match sorted(counts.values()):
            case [1, 1, 1, 1, 1]:
                hand = 0
            case [1, 1, 1, 2]:
                hand = 1
            case [1, 2, 2]:
                hand = 2
            case [1, 1, 3]:
                hand = 3
            case [2, 3]:
                hand = 4
            case [1, 4]:
                hand = 5
            case [5]:
                hand = 6
            case _:
                raise ValueError(f"Invalid hand {cards}")
        hands.append((hand, *cards, bid))
    return hands


def main():
    hands = read_input()
    hands.sort()
    sum_ = 0
    for i, (hand, *cards, bid) in enumerate(hands):
        sum_ += bid * (i + 1)
    print(sum_)


if __name__ == "__main__":
    main()
