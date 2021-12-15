"""AoC 14, 2021: Extended Polymerization"""
import copy
import itertools
from collections import Counter

from aocd import get_data

InputType = list[tuple[str, dict[str, str]]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    batches = puzzle_input.split("\n\n")
    polymer = batches[0]
    return polymer, {
        k: v
        for k, v in (tuple(line.split(" -> ")) for line in batches[1].split("\n"))
    }


def grow(n: int, data: InputType) -> OutputType:
    polymer = data[0]
    c = Counter(zip(polymer[:-1], polymer[1:]))
    for _ in range(n):
        d = Counter()
        for (a, b), v in c.items():
            n = data[1][a + b]
            d[a + n] += v
            d[n + b] += v
        c = d
    d = Counter()
    for (a, b), v in c.items():
        d[a] += v
    d[polymer[-1]] += 1
    return d.most_common()[0][1] - d.most_common()[-1][1]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return grow(10, data)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    return grow(40, data)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=14))
    print("\n".join(solve(data)))
