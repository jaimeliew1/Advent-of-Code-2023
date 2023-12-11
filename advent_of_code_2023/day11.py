from pathlib import Path
from itertools import combinations

INPUT_FN = Path(__file__).parent.parent / "input/day11.txt"


def parse(fn: Path) -> list[str]:
    return [line.strip() for line in open(fn).readlines()]


def expand(input):
    out = []
    for row in input:
        out.append(row)
        if all(x == "." for x in row):
            out.append(row)

    return out


def solve(input: list[str]) -> tuple[int, int]:
    expanded = expand(zip(*expand(input)))
    galaxies = []
    for i, row in enumerate(expanded):
        for j, col in enumerate(row):
            if col == "#":
                galaxies.append((i, j))

    ans1 = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, r=2):
        ans1 += abs(x1 - x2) + abs(y1 - y2)

    ans2 = 0

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
