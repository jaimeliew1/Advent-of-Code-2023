from pathlib import Path

INPUT_FN = Path(__file__).parent.parent / "input/day03.txt"
deltas = [(1, 1), (1, 0), (1, -1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]


def parse(fn: Path) -> list[tuple[int, bool, list]]:
    with open(fn) as f:
        raw_lines = [x.strip() for x in f.readlines()]
    N = len(raw_lines[0])
    # Pad input with ...
    lines = [N * "."] + ["." + x + "." for x in raw_lines] + [N * "."]

    # Collect all numbers, their neighbors, and gear location in a list of tuples.
    out = []
    for y, line in enumerate(lines):
        current, has_neighbors, gear_coord = [], False, set()
        for x, char in enumerate(line):
            if char.isnumeric():
                # Collect digit
                current.append(char)
                # Check for neighbors
                has_neighbors |= any(
                    map(
                        lambda x: not x.isnumeric() and x != ".",
                        [lines[y + dy][x + dx] for (dx, dy) in deltas],
                    )
                )
                # record gears if there are any.
                gear_coord.update(
                    filter(
                        lambda z: lines[z[0]][z[1]] == "*",
                        ((y + dy, x + dx) for (dx, dy) in deltas),
                    )
                )
            elif len(current) > 0:
                # If we've reached the end of a number, save it.
                out.append((int("".join(current)), has_neighbors, list(gear_coord)))
                current, has_neighbors, gear_coord = [], False, set()

    return out


def solve(input: list[tuple[int, bool, list]]) -> tuple[int, int]:
    ans1 = sum(map(lambda x: x[0], filter(lambda x: x[1], input)))

    # Invert dictionary of gear locations.
    gears = {}
    for num, _, gear in filter(lambda x: len(x[2]) > 0, input):
        if gear[0] not in gears:
            gears[gear[0]] = [num]
        else:
            gears[gear[0]].append(num)

    ans2 = sum(a * b for a, b in filter(lambda x: len(x) == 2, gears.values()))

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
