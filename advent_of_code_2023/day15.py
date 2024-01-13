from pathlib import Path

INPUT_FN = Path(__file__).parent.parent / "input/day15.txt"


def parse(fn: Path) -> list[str]:
    with open(fn) as f:
        return f.read().split(",")


def hash(input: str) -> int:
    out = 0
    for c in input:
        out = ((out + ord(c)) * 17) % 256
    return out


def solve(input: list[str]) -> tuple[int, int]:
    ans1 = sum(hash(x) for x in input)

    boxes = [[] for _ in range(256)]
    for command in input:
        if "-" in command:
            label = command[:-1]
            box = hash(label)
            boxes[box] = [(l, focal) for (l, focal) in boxes[box] if l != label]
        elif "=" in command:
            label, focal = command[:-2], int(command[-1])
            box = hash(label)
            if any(l == label for (l, focal) in boxes[box]):
                boxes[box] = [(l, focal if l == label else f) for (l, f) in boxes[box]]
            else:
                boxes[box].append((label, focal))

    ans2 = 0
    for i, box in enumerate(boxes):
        for j, (_, lens) in enumerate(box):
            ans2 += (i + 1) * (j + 1) * lens
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
