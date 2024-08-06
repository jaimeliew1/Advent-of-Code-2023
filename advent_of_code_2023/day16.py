from pathlib import Path


INPUT_FN = Path(__file__).parent.parent / "input/day16.txt"


def parse(fn: Path) -> dict[complex, str]:
    map = {}
    for j, line in enumerate(open(fn)):
        for i, c in enumerate(line.strip()):
            map[complex(i, j)] = c
    return map


def calc_visited(to_do: list[complex], map: dict[complex, str]) -> int:
    visited = set()
    while to_do:
        pos, dir = to_do.pop()
        while (pos, dir) not in visited:
            visited.add((pos, dir))
            pos += dir
            match map.get(pos):
                case "/":
                    dir = -complex(dir.imag, dir.real)
                case "\\":
                    dir = complex(dir.imag, dir.real)
                case "-":
                    dir = 1
                    to_do.append((pos, -1))
                case "|":
                    dir = 1j
                    to_do.append((pos, -1j))
                case None:
                    break
    return len(set(x[0] for x in visited)) - 1


def solve(input: dict[complex, str]) -> tuple[int, int]:

    ans1, ans2 = calc_visited([(-1, 1)], input), 0
    for pos in input:
        for dir in (1, -1, 1j, -1j):
            if (pos - dir) not in input:
                ans2 = max(ans2, calc_visited([(pos - dir, dir)], input))

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
