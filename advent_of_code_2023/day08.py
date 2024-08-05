from pathlib import Path
from itertools import cycle
from math import lcm

INPUT_FN = Path(__file__).parent.parent / "input/day08.txt"

directions = {"L": 0, "R": 1}


def parse(fn: Path) -> tuple[str, dict]:
    commands, map, *_ = open(fn).read().split("\n\n")
    map = (
        map.replace("=", "")
        .replace("(", "")
        .replace(")", "")
        .replace(",", "")
        .split("\n")
    )
    map = {x.split()[0]: (x.split()[1], x.split()[2]) for x in map}

    return commands, map


def steps_to_end(current: str, commands: str, map: dict) -> int:
    steps = 0
    for com in cycle(commands):
        current = map[current][directions[com]]
        steps += 1
        if current.endswith("Z"):
            return steps


def solve(input: tuple[str, dict]) -> tuple[int, int]:
    commands, map = input

    starts = [x for x in map.keys() if x.endswith("A")]
    cycle_lengths = [steps_to_end(start, commands, map) for start in starts]

    return steps_to_end("AAA", commands, map), lcm(*cycle_lengths)


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
