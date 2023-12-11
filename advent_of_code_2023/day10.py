from pathlib import Path


INPUT_FN = Path(__file__).parent.parent / "input/day10.txt"
deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
pipes: dict[str, list] = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
}


def parse(fn: Path) -> list[str]:
    return [line.strip() for line in open(fn).readlines()]


def solve(input: list[str]) -> tuple[int, int]:
    start = next(
        ((i, j) for i, line in enumerate(input) if (j := line.find("S")) != -1)
    )
    direction = next(
        (dx, dy)
        for dx, dy in deltas
        if (-dx, -dy) in pipes[input[start[0] + dx][start[1] + dy]]
    )

    visited = [start]
    current = (start[0] + direction[0], start[1] + direction[1])
    double_area = 0
    while (this_pipe := input[current[0]][current[1]]) != "S":
        direction = next(
            (dx, dy)
            for dx, dy in pipes[this_pipe]
            if (dx, dy) != (-direction[0], -direction[1])
        )
        # Shoelace formula
        double_area += (visited[-1][0] - current[0]) * (visited[-1][1] + current[1])
        visited.append(current)
        current = (current[0] + direction[0], current[1] + direction[1])

    ans1 = len(visited) // 2
    # Pick's theorem
    ans2 = -ans1 + double_area // 2 + 1

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
