"""AoC 2, 2020: Password Philosophy"""

from aocd import get_data

InputType = list[tuple[int, int, str, str]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    ret = []
    for line in puzzle_input.split("\n"):
        range_, letter, password = line.split(" ", 2)
        ret.append((*map(int, range_.split("-")), letter.rstrip(":"), password))
    return ret


def part1(data: InputType) -> OutputType:
    """Solve part 1."""


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
    data = parse(get_data(year=2020, day=2))
    print("\n".join(solve(data)))
