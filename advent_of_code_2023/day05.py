from pathlib import Path
from tqdm import trange

INPUT_FN = Path(__file__).parent.parent / "input/day05.txt"


def parse(fn: Path) -> tuple[list[int], list[list[tuple[int, ...]]]]:
    raw = open(fn).read()
    seeds = [int(x) for x in raw.split("\n")[0].split(":")[1].split()]

    maps = []
    for block in raw.split("\n\n")[1:]:
        map = [tuple(int(x) for x in line.split()) for line in block.split("\n")[1:]]
        maps.append(map)

    return seeds, maps


def solve(input: tuple[list[int], list[list[tuple[int, ...]]]]) -> tuple[int, int]:
    ans1 = int(1e10)
    seeds, maps = input
    for seed in seeds:
        val = seed
        for map in maps:
            match [a + val - b for a, b, c in map if val > b and val < b + c]:
                case [num]:
                    val = num

        ans1 = min(ans1, val)

    ans2 = int(1e10)
    for start, length in zip(seeds[::2], seeds[1::2]):
        for seed in trange(start, start + length):
            val = seed
            for map in maps:
                match [a + val - b for a, b, c in map if val > b and val < b + c]:
                    case [num]:
                        val = num

            ans2 = min(ans2, val) # lol
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
