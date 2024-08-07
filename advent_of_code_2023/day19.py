from functools import reduce
from pathlib import Path
import re


INPUT_FN = Path(__file__).parent.parent / "input/day19.txt"


def parse(fn: Path) -> tuple[list]:
    filters_raw, parts_raw = open(fn).read().split("\n\n")
    filters = {}
    for filter in filters_raw.split():
        key, _filters = filter.split("{")
        filters[key] = [
            (f[0], f[1], int(f[2:].split(":")[0]), f[2:].split(":")[1])
            for f in _filters.split(",")[:-1]
        ] + [("a", ">", -999, _filters.split(",")[-1][:-1])]

    parts = []
    for part in parts_raw.split():
        temp = [int(x) for x in re.findall(r"\d+", part)]
        parts.append({"x": temp[0], "m": temp[1], "a": temp[2], "s": temp[3]})

    return filters, parts


def recurse(pos: str, ranges: dict, filters: dict) -> int:
    combinations = 0
    if pos == "A":
        return reduce(lambda x, y: x * y, [b - a + 1 for a, b in ranges.values()])
    elif pos == "R":
        return 0

    for att, comm, thres, goto in filters[pos]:
        match comm:
            case "<":
                combinations += recurse(
                    goto,
                    dict(
                        ranges,
                        **{att: (ranges[att][0], min(ranges[att][1], thres - 1))},
                    ),
                    filters,
                )
                ranges[att] = (max(ranges[att][0], thres), ranges[att][1])
            case ">":
                combinations += recurse(
                    goto,
                    dict(
                        ranges,
                        **{att: (max(ranges[att][0], thres + 1), ranges[att][1])},
                    ),
                    filters,
                )
                ranges[att] = (ranges[att][0], min(ranges[att][1], thres))

    return combinations


def solve(input: tuple[list]) -> int:
    filters, parts = input
    ans1 = 0
    for part in parts:
        pos = "in"
        while pos not in ["A", "R"]:
            for att, comm, thres, goto in filters[pos]:
                condition = part[att] < thres if comm == "<" else part[att] > thres
                if condition:
                    pos = goto
                    break
        if pos == "A":
            ans1 += sum(part.values())

    ranges = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    return ans1, recurse("in", ranges, filters)


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
