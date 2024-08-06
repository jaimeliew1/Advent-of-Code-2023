from pathlib import Path

INPUT_FN = Path(__file__).parent.parent / "input/day14.txt"


def parse(fn: Path) -> list[str]:
    return [[char for char in s] for s in (x.strip() for x in open(fn).readlines())]


def roll(input: list[str]) -> list[str]:
    out = [input[0]]
    for i in range(1, len(input)):
        out.append([])
        for j in range(len(input[i])):
            if input[i][j] == "O" and input[i - 1][j] == ".":
                out[i].append(".")
                out[i - 1][j] = "O"
            else:
                out[i].append(input[i][j])
    return out


def tilt(input: list[str]) -> list[str]:
    output = [list(inner_list[:]) for inner_list in input]
    while (new := roll(output)) != output:
        output = new
    return output


def cycle(input: list[str]) -> list[str]:
    input = tilt(input)
    input = list(zip(*tilt(list(zip(*input)))))
    input = list(tilt(list(input[::-1]))[::-1])
    return list(zip(*tilt(list(zip(*input))[::-1])[::-1]))


def score(x):
    return sum((i + 1) * sum(c == "O" for c in row) for i, row in enumerate(x[::-1]))


def solve(input: list[str]) -> tuple[int, int]:
    ans1 = score(tilt(input))

    seen_hashes, scores = [], []
    while True:  # Keep rolling until a cycle is found.
        input = cycle(input)
        _hash = hash(tuple(tuple(inner_list) for inner_list in input))
        if _hash not in seen_hashes:
            seen_hashes.append(_hash)
            scores.append(score(input))
        else:
            start = seen_hashes.index(_hash)
            cycle_length = len(seen_hashes) - start
            break

    ans2 = scores[(1000000000 - start) % cycle_length + start - 1]
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse(INPUT_FN)))
