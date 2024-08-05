from dataclasses import dataclass
from functools import reduce
from pathlib import Path
from typing import Optional

INPUT_FN = Path(__file__).parent.parent / "input/day05.txt"


@dataclass
class RangeMap:
    in_a: int
    in_b: int
    out_a: int
    out_b: int

    def map(self, val) -> Optional[float]:
        if (val >= self.in_a) and (val < self.in_b):
            return val - self.in_a + self.out_a
        return None

    def reverse_map(self, val) -> float:
        if (val >= self.out_a) and (val < self.out_b):
            return val - self.out_a + self.in_a
        return None


@dataclass
class RangeMaps:
    maps: list[RangeMap]

    def map(self, val) -> float:
        out = [x for map in self.maps if (x := map.map(val)) is not None]
        return out[0] if len(out) > 0 else val

    def reverse_map(self, val) -> float:
        out = [x for map in self.maps if (x := map.reverse_map(val)) is not None]
        return out[0] if len(out) > 0 else val


def parse(fn: Path) -> tuple[list[int], list[RangeMaps]]:
    raw = open(fn).read()
    seeds = [int(x) for x in raw.split("\n")[0].split(":")[1].split()]

    maps = []
    for block in raw.split("\n\n")[1:]:
        _maps = []
        for line in block.split("\n")[1:]:
            a, b, c = (int(x) for x in line.split())
            _maps.append(RangeMap(b, b + c, a, a + c))

        maps.append(RangeMaps(_maps))

    return seeds, maps


def solve(input: tuple[list[int], list[RangeMaps]]) -> tuple[int, int]:
    seeds, maps = input
    ans1, ans2 = 1e10, 1e10

    for seed in seeds:
        ans1 = min(ans1, reduce(lambda v, map: map.map(v), maps, seed))

    targets = []
    for map in maps[::-1]:
        targets = (
            [x.reverse_map(x.out_a) for x in map.maps]
            + [x.in_a for x in map.maps]
            + [map.reverse_map(val) for val in targets]
        )
    targets.extend([seeds[i] for i in range(0, len(seeds), 2)])

    in_range_targets = []
    for i in range(0, len(seeds), 2):
        in_range_targets.extend(
            [x for x in targets if (x >= seeds[i]) and (x < seeds[i] + seeds[i + 1])]
        )

    for seed in in_range_targets:
        ans2 = min(ans2, reduce(lambda v, map: map.map(v), maps, seed))

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
