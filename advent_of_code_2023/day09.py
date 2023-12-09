from pathlib import Path
import numpy as np

INPUT_FN = Path(__file__).parent.parent / "input/day09.txt"


def parse(fn: Path) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in open(fn).readlines()]


def extrapolate(line: list) -> int:
    diffs = [line]
    while not all(x == 0 for x in diffs[-1]):
        diffs.append(list(np.diff(diffs[-1])))

    diffs[-1].append(0)
    N = len(diffs)
    for i in range(1, N):
        diffs[N - i - 1].append(diffs[N - i - 1][-1] + diffs[N - i][-1])
    return diffs[0][-1]


def solve(input: list[list[int]]) -> tuple[int, int]:
    ans1 = sum(extrapolate(line) for line in input)
    ans2 = sum(extrapolate(line[::-1]) for line in input)

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
