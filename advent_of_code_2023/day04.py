from pathlib import Path

INPUT_FN = Path(__file__).parent.parent / "input/day04.txt"


def parse(fn: Path) -> list[tuple[set[int], set[int]]]:
    out = []
    lines = [x.rsplit(":")[1] for x in open(fn).readlines()]
    for line in lines:
        a, b = line.split("|")
        out.append((set(int(x) for x in a.split()), set(int(x) for x in b.split())))

    return out


def solve(input: list[tuple[set[int], set[int]]]) -> tuple[int, int]:
    ans1, quantity = 0, [1] * len(input)

    for i, (lottery, mynumbers) in enumerate(input):
        ans1 += int(2 ** (n_overlap := len(lottery & mynumbers) - 1))

        for j in range(n_overlap):
            quantity[i + j + 1] += quantity[i]

    ans2 = sum(quantity)
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
