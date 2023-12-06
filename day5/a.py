from dataclasses import dataclass


@dataclass
class MapRange:
    dst_start: int
    src_start: int
    length: int

    def includes(self, value: int) -> bool:
        return self.src_start <= value < self.src_start + self.length

    def apply(self, value: int) -> int:
        assert self.includes(value)
        return self.dst_start + value - self.src_start


class MultiMap:
    def __init__(self, maps: list[MapRange]):
        maps.sort(key=lambda x: x.length, reverse=True)
        self.maps = maps

    def apply(self, value: int) -> int:
        for m in self.maps:
            if m.includes(value):
                return m.apply(value)
        return value


def read_input():
    with open("input.txt") as f:
        content = f.read()

    blocks = content.split("\n\n")

    seeds = [int(x) for x in blocks[0].split(":")[1].strip().split(" ")]

    maps = {}
    for block in blocks[1:]:
        title, content = block.split(":")
        maps[title.split(" ")[0]] = MultiMap([MapRange(*[int(x) for x in line.split(" ")]) for line in content.strip().split("\n")])

    return seeds, maps


def main():
    seeds, maps = read_input()
    locations = []
    for seed in seeds:
        # print(f"{seed=}")
        soil = maps["seed-to-soil"].apply(seed)
        # print(f"{soil=}")
        fertilizer = maps["soil-to-fertilizer"].apply(soil)
        # print(f"{fertilizer=}")
        water = maps["fertilizer-to-water"].apply(fertilizer)
        # print(f"{water=}")
        light = maps["water-to-light"].apply(water)
        # print(f"{light=}")
        temperature = maps["light-to-temperature"].apply(light)
        # print(f"{temperature=}")
        humidity = maps["temperature-to-humidity"].apply(temperature)
        # print(f"{humidity=}")
        location = maps["humidity-to-location"].apply(humidity)
        # print(f"{location=}")
        locations.append(location)
    print(min(locations))


if __name__ == "__main__":
    main()
