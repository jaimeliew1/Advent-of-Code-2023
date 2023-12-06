from pathlib import Path
import numpy as np

INPUT_FN = Path(__file__).parent.parent / "input/day06.txt"


def parse(fn: Path) -> tuple[str, ...]:
    return tuple(x.split(":")[1].strip() for x in open(fn).readlines())


def n_ways(time, distance):
    center, width = time / 2, np.sqrt(time**2 - 4 * distance) / 2
    return np.ceil(center + width) - np.floor(center - width) - 1


def solve(input: tuple[str, ...]) -> tuple[int, int]:
    ans1 = np.prod(
        [n_ways(int(t), int(d)) for t, d in zip(input[0].split(), input[1].split())]
    )
    ans2 = n_ways(int(input[0].replace(" ", "")), int(input[1].replace(" ", "")))
    return int(ans1), int(ans2)


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
