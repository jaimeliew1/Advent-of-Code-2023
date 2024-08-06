from functools import cache
from pathlib import Path

INPUT_FN = Path(__file__).parent.parent / "input/day12.txt"


def parse(fn: Path) -> list[tuple[str, tuple[int]]]:
    with open(fn) as f:
        return [
            (record, tuple(map(int, lengths.split(","))))
            for record, lengths in (line.strip().split() for line in f)
        ]


@cache
def valid_arrangements(record: str, counts: tuple[int]) -> int:
    record = record.lstrip(".") # left .'s are redundant.

    if len(record) == 0: # empty record is valid of no more counts.
        return int(len(counts) == 0)
    elif len(counts) == 0: # empty count is valid of no more springs.
        return int("#" not in record)
    elif record[0] == "#":
        if len(record) < counts[0] or "." in record[: counts[0]]:
            return 0 # invalid record not long enough or short spring length.
        elif len(record) == counts[0]:
            return int(len(counts) == 1) # valid if record length matches final count.
        elif record[counts[0]] == "#":
            return 0 # invalid of spring is too long.
        else:
            return valid_arrangements(record[counts[0] + 1 :], counts[1:]) # check remaining record.
    elif record[0] == "?":
        return valid_arrangements("." + record[1:], counts) + valid_arrangements(
            "#" + record[1:], counts
        ) # fork if ? is next in record.


def solve(input: list[tuple[str, tuple[int]]]) -> tuple[int, int]:
    ans1 = sum([valid_arrangements(record, lengths) for record, lengths in input])
    ans2 = sum(
        [valid_arrangements("?".join([r for _ in range(5)]), 5 * l) for r, l in input]
    )
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
