from pathlib import Path

INPUT_FN = Path(__file__).parent.parent / "input/day18.txt"


def parse(fn: Path) -> tuple[list]:
    directions, distances, hexes = [], [], []
    for line in open(fn):
        dir, dist, h = line.split()
        directions.append(dir)
        distances.append(int(dist))
        hexes.append(h[2:-1])
    return directions, distances, hexes


def calc_volume(directions: list[str], distances: list[int]) -> int:
    area, perimeter, x, y = 0, 0, 0, 0
    for dir, distance in zip(directions, distances):
        match dir:
            case "R" | 0:
                dx, dy = distance, 0
            case "L" | 2:
                dx, dy = -distance, 0
            case "U" | 3:
                dx, dy = 0, distance
            case "D" | 1:
                dx, dy = 0, -distance

        area += (y + dy) * dx  # Shoelace formula
        perimeter += distance
        x, y = x + dx, y + dy

    return area + perimeter // 2 + 1  # Pick's theorem


def solve(input: tuple[list]) -> tuple[int, int]:
    directions, distances, hexes = input
    ans1 = calc_volume(directions, distances)
    ans2 = calc_volume([int(h[-1]) for h in hexes], [int(h[:-1], 16) for h in hexes])
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
