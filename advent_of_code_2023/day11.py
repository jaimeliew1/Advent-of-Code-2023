from pathlib import Path
from itertools import combinations

INPUT_FN = Path(__file__).parent.parent / "input/day11.txt"


def parse(fn: Path) -> list[str]:
    return [line.strip() for line in open(fn).readlines()]


def empty_indices(input):
    indices = []
    for i, row in enumerate(input):
        if all(x == "." for x in row):
            indices.append(i)

    return indices


def solve(input: list[str]) -> tuple[int, int]:
    empty_rows = empty_indices(input)
    empty_cols = empty_indices(zip(*input))

    galaxies = []
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if col == "#":
                galaxies.append((i, j))

    ans1, ans2 = 0, 0
    for (x1, y1), (x2, y2) in combinations(galaxies, r=2):
        expanded = sum(
            [(coord >= min(y1, y2)) and (coord < max(y1, y2)) for coord in empty_cols]
        ) + sum(
            [(coord >= min(x1, x2)) and (coord < max(x1, x2)) for coord in empty_rows]
        )

        ans1 += abs(x1 - x2) + abs(y1 - y2) + expanded * (2 - 1)
        ans2 += abs(x1 - x2) + abs(y1 - y2) + expanded * (1000000 - 1)

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
