from pathlib import Path
from rich import print

INPUT_FN = Path(__file__).parent.parent / "input/day17.txt"


def parse(fn: Path) -> dict[complex, int]:
    return {
        complex(i, j): int(c)
        for j, line in enumerate(open(fn))
        for i, c in enumerate(line.strip())
    }


def hottest_path(_min: int, _max: int, end: complex, map: dict[complex, int]) -> int:
    frontier = {(0, 1j): 0, (0, 1): 0}
    visited = set()
    while frontier:
        pos, dir = min(frontier, key=lambda x: frontier[x])
        heat_loss = frontier.pop((pos, dir))

        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))
        if pos == end:
            return heat_loss

        for new_dir in [1j / dir, -1j / dir]:
            for distance in range(_min, _max + 1):
                if (new_pos := pos + new_dir * distance) not in map:
                    continue

                new_heatloss = heat_loss + sum(
                    map[pos + new_dir * d] for d in range(1, distance + 1)
                )
                if old_heatloss := frontier.get((new_pos, new_dir)):
                    frontier[(new_pos, new_dir)] = min(new_heatloss, old_heatloss)
                else:
                    frontier[(new_pos, new_dir)] = new_heatloss


def solve(input: dict[complex, int]) -> tuple[int, int]:
    ans1 = hottest_path(1, 3, [*input][-1], input)
    ans2 = hottest_path(4, 10, [*input][-1], input)
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
