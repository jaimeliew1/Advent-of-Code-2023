from pathlib import Path
from collections import Counter
from dataclasses import dataclass


INPUT_FN = Path(__file__).parent.parent / "input/day07.txt"

card_vals = {str(i): i for i in range(2, 10)} | {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


@dataclass
class Hand:
    hand: str
    bet: int

    def __lt__(self, other) -> bool:
        if (rank1 := self.rank()) == (rank2 := other.rank()):
            for c1, c2 in zip(self.hand, other.hand):
                if c1 == c2:
                    continue

                return card_vals[c1] < card_vals[c2]

        return rank1 < rank2

    def rank(self) -> int:
        match sorted(Counter(self.hand).values()):
            case [5]:
                return 6
            case [1, 4]:
                return 5
            case [2, 3]:
                return 4
            case [*_, 3]:
                return 3
            case [1, 2, 2]:
                return 2
            case [*_, 2]:
                return 1
            case _:
                return 0


def parse(fn: Path) -> list[Hand]:
    return [
        Hand(line.split()[0], int(line.split()[1])) for line in open(fn).readlines()
    ]


def solve(input: list[Hand]) -> tuple[int, int]:
    ans1 = sum((i + 1) * hand.bet for i, hand in enumerate(sorted(input)))
    ans2 = 0

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
