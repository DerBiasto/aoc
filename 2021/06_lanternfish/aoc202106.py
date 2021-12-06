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
    for _ in range(num_days):
        temp = c[0]
        c[0] = c[1]
        c[1] = c[2]
        c[2] = c[3]
        c[3] = c[4]
        c[4] = c[5]
        c[5] = c[6]
        c[6] = c[7] + temp
        c[7] = c[8]
        c[8] = temp
    return sum(c.values())


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
