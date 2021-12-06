"""AoC 6, 2021: Lanternfish"""
from collections import Counter

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return list(map(int, puzzle_input.split(",")))


def model_lanternfish(data: InputType, num_days: int) -> int:
    c = Counter(data)
    d = [c[i] for i in range(9)]
    for _ in range(num_days):
        d.append(d.pop(0))
        d[6] += d[-1]
    return sum(d)


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return model_lanternfish(data, 80)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    return model_lanternfish(data, 256)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=6))
    print("\n".join(solve(data)))
