from pathlib import Path

INPUT_FN = Path(__file__).parent.parent / "input/day04.txt"


def parse(fn: Path) -> list[tuple[list[int], list[int]]]:
    out = []
    lines = [x.rsplit(":")[1] for x in open(fn).readlines()]
    for line in lines:
        a, b = line.split("|")
        out.append(([int(x) for x in a.split()], [int(x) for x in b.split()]))

    return out


def solve(input: list[tuple[list[int], list[int]]]) -> tuple[int, int]:
    ans1 = 0
    for lottery, mynumbers in input:
        n_overlap = len(set(lottery).intersection(mynumbers))
        ans1 += int(2 ** (n_overlap - 1))
    ans2 = 0
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
