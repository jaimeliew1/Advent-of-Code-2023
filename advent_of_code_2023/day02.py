from pathlib import Path

INPUT_FN = Path(__file__).parent.parent / "input/day02.txt"


def parse(fn: Path) -> list[str]:
    with open(fn) as f:
        return [line.rsplit(":")[1] for line in f.readlines()]


def min_count(line: str) -> dict[str, int]:
    colors = {"red": 0, "green": 0, "blue": 0}
    for substring in line.rstrip().replace(";", ",").split(","):
        quant, c = substring.strip().rsplit(" ")
        colors[c] = max(colors[c], int(quant))
    return colors


color_lim = {"red": 12, "green": 13, "blue": 14}
def solve(input: list[str]) -> tuple[int, int]:
    ans1 = 0
    for i, line in enumerate(input):
        colors = min_count(line)
        if all(colors[c] <= color_lim[c] for c in ("red", "green", "blue")):
            ans1 += i + 1

    ans2 = sum(c["red"] * c["green"] * c["blue"] for c in (min_count(line) for line in input))
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
