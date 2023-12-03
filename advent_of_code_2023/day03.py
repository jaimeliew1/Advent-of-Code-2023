from pathlib import Path

INPUT_FN = Path(__file__).parent.parent / "input/day03.txt"
deltas = [(1, 1), (1, 0), (1, -1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

def parse(fn: Path) -> list[tuple[int, bool, list]]:
    with open(fn) as f:
        raw_lines = [x.strip() for x in f.readlines()]
    N = len(raw_lines[0])
    # Pad input
    lines = [N * "."] + ["." + x + "." for x in raw_lines] + [N * "."]

    # Collect all numbers, their neighbors, and gear location in a list of tuples.
    out = []
    for y, line in enumerate(lines):
        current, has_neighbors, gear_coord = [], False, set()
        for x, char in enumerate(line):
            if char.isnumeric():
                current.append(char)
                has_neighbors |= any(_char not in ".0123456789" for _char in [lines[y + dy][x + dx] for (dx, dy) in deltas])
                gear_coord.update((y + dy, x + dx) for (dx, dy) in deltas if lines[y + dy][x + dx] == "*")

            elif len(current) > 0:
                # If we've reached the end of a number, save it.
                out.append((int("".join(current)), has_neighbors, list(gear_coord)))
                current, has_neighbors, gear_coord = [], False, set()

    return out


def solve(input: list[tuple[int, bool, list]]) -> tuple[int, int]:
    ans1 = sum(num for num, has_neighbors, _ in input if has_neighbors)


    gears = {}
    for num, _, gear in filter(lambda x: len(x[2]) > 0, input):
        gears[gear[0]] = gears.get(gear[0], []) + [num]
    ans2 = sum(a * b for a, b in filter(lambda x: len(x) == 2, gears.values()))

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))