from dataclasses import dataclass


@dataclass
class Range:
    start: int
    end: int

    def overlaps(self, other: "Range") -> bool:
        return self.start <= other.end and other.start <= self.end

    @classmethod
    def combine(cls, a: "Range", b: "Range") -> "Range":
        assert a.overlaps(b)
        return cls(min(a.start, b.start), max(a.end, b.end))


@dataclass
class RangeMap:
    dst_start: int
    src_start: int
    length: int

    @property
    def src_end(self):
        return self.src_start + self.length

    @property
    def dst_end(self):
        return self.dst_start + self.length

    def includes(self, range_: Range) -> bool:
        return (
            self.src_start <= range_.start < self.src_end
            and self.src_start < range_.end <= self.src_end
        )

    def apply(self, range_: Range) -> Range:
        assert self.includes(range_), f"{self=} {range_=}"
        offset = self.dst_start - self.src_start
        return Range(range_.start + offset, range_.end + offset)


class MultiMap:
    def __init__(self, maps: list[RangeMap]):
        maps.sort(key=lambda x: x.src_start, reverse=False)
        for i in range(len(maps) - 1):
            assert maps[i].src_end <= maps[i + 1].src_start
        self.maps = maps

    def map(self, ranges: list[Range]) -> list[Range]:
        result = []
        ranges = ranges.copy()
        while ranges:
            r = ranges.pop(0)
            for m in self.maps:
                if r.end <= m.src_start or m.src_end <= r.start:
                    continue
                result.append(m.apply(Range(max(r.start, m.src_start), min(r.end, m.src_end))))
                if r.end > m.src_end:
                    ranges.insert(0, Range(m.src_end, r.end))
                if r.start < m.src_start:
                    ranges.insert(0, Range(r.start, m.src_start))
                break
            else:
                result.append(r)
        result.sort(key=lambda x: (x.start, x.end), reverse=False)
        result_combined = [result[0]]
        for r in result[1:]:
            if result_combined[-1].overlaps(r):
                result_combined[-1] = Range.combine(result_combined[-1], r)
            else:
                result_combined.append(r)
        return result_combined


def read_input():
    with open("input.txt") as f:
        content = f.read()

    blocks = content.split("\n\n")

    seeds = [int(x) for x in blocks[0].split(":")[1].strip().split(" ")]
    seeds = [Range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    maps = {}
    for block in blocks[1:]:
        title, content = block.split(":")
        maps[title.split(" ")[0]] = MultiMap(
            [
                RangeMap(*[int(x) for x in line.split(" ")])
                for line in content.strip().split("\n")
            ]
        )

    return seeds, maps


def main():
    seeds, maps = read_input()
    print(f"{seeds=}")
    soils = maps["seed-to-soil"].map(seeds)
    print(f"{soils=}")
    fertilizers = maps["soil-to-fertilizer"].map(soils)
    print(f"{fertilizers=}")
    waters = maps["fertilizer-to-water"].map(fertilizers)
    print(f"{waters=}")
    lights = maps["water-to-light"].map(waters)
    print(f"{lights=}")
    temperatures = maps["light-to-temperature"].map(lights)
    print(f"{temperatures=}")
    humiditys = maps["temperature-to-humidity"].map(temperatures)
    print(f"{humiditys=}")
    locations = maps["humidity-to-location"].map(humiditys)
    print(f"{locations=}")
    print(locations[0].start)


if __name__ == "__main__":
    main()
