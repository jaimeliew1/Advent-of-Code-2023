from pathlib import Path
from typing import List, Dict, Tuple

INPUT_FN = Path(__file__).parent.parent / "input/day01.txt"

numbers = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
numbers_2 = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse(fn: Path) -> List[str]:
    with open(fn) as f:
        return f.readlines()


def firstoccurence(of, string: str) -> str:
    while len(string) > 0:
        for tofind in of:
            if string.startswith(tofind):
                return tofind
        string = string[1:]

    raise ValueError


def calibration_value(string: str, numbers: Dict[str, int]) -> int:
    first = firstoccurence(numbers.keys(), string)
    last = firstoccurence([x[::-1] for x in numbers.keys()], string[::-1])[::-1]
    return 10 * numbers[first] + numbers[last]


def solve(input: List[str]) -> Tuple[int, int]:
    ans1 = sum(calibration_value(line, numbers) for line in input)
    numbers.update(numbers_2)
    ans2 = sum(calibration_value(line, numbers) for line in input)

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
