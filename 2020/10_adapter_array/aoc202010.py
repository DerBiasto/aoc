"""AoC 10, 2020: Adapter Array"""
from collections import Counter

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        int(line)
        for line in puzzle_input.split("\n")
    ]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    sorted_joltages = [0] + sorted(data)
    sorted_joltages.append(sorted_joltages[-1] + 3)
    c = Counter(map(lambda i: sorted_joltages[i + 1] - sorted_joltages[i], range(0, len(sorted_joltages) - 1)))
    return c[1] * c[3]


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    sorted_joltages = [0] + sorted(data)
    sorted_joltages.append(sorted_joltages[-1] + 3)
    seq = "".join(map(lambda i: str(sorted_joltages[i + 1] - sorted_joltages[i]), range(0, len(sorted_joltages) - 1)))
    sub_seqs = [s for s in seq.split("3") if s]
    sub_lengths = [len(s) - 1 for s in sub_seqs]
    ret = 1
    for e in sub_lengths:
        if e <= 2:
            ret *= 1 << e
        else:
            ret *= (1 << e) - 1
    return ret


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=10))
    print("\n".join(solve(data)))
