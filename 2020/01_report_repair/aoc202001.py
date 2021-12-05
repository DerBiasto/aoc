"""AoC 1, 2020: Report Repair"""

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return list(map(int, puzzle_input.split("\n")))


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    values = set(data)
    for val in data:
        num = 2020 - val
        if num in values:
            return num * val


def part2(data: InputType) -> OutputType:
    """Solve part 2."""


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=1))
    print("\n".join(solve(data)))
