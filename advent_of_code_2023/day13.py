from pathlib import Path

INPUT_FN = Path(__file__).parent.parent / "input/day13.txt"


def parse(fn: Path) -> list[list[str]]:
    return [x.split() for x in open(fn).read().split("\n\n")]


def symmetry(s: list[str], target_smudge_count: int = 0) -> int:
    for i in range(1, len(s)):
        smudge_count = sum(
            sum(1 for a, b in zip(s1, s2) if a != b)
            for s1, s2 in zip(s[:i][::-1], s[i:])
        )
        if smudge_count == target_smudge_count:
            return i
    return 0


def solve(input: list[list[str]]) -> tuple[int, int]:
    ans1, ans2 = 0, 0
    for x in input:
        ans1 += 100 * symmetry(x) + symmetry(["".join(a) for a in zip(*x)])
        ans2 += 100 * symmetry(x, 1) + symmetry(["".join(a) for a in zip(*x)], 1)
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
