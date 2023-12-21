from pathlib import Path
from itertools import product

INPUT_FN = Path(__file__).parent.parent / "input/day12.txt"


def parse(fn: Path) -> list[list[str]]:
    return [line.strip().split(" ") for line in open(fn).readlines()]


def arrangement_gen(record: str):
    all_strings = list(product(["#", "."], repeat=record.count("?")))
    indices = [i for i, v in enumerate(record) if v == "?"]
    for arrangement in all_strings:
        out = list(record)
        for i, v in zip(indices, arrangement):
            out[i] = v

        yield "".join(out)


def count_lengths(record: str) -> list[int]:
    return list(len(x) for x in record.split(".") if len(x) > 0)


def solve(input: list[list[str]]) -> tuple[int, int]:
    ans1 = 0
    for record in input:
        lengths = [int(x) for x in record[1].split(",")]
        counts = sum(1 for a in arrangement_gen(record[0]) if count_lengths(a) == lengths)

        ans1 += counts

    return ans1, 0


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
