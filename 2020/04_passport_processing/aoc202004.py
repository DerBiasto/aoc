"""AoC 4, 2020: Passport Processing"""

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    ret = []
    for passport in puzzle_input.split("\n\n"):
        kv_pairs = passport.split()
        ret.append(dict([kv.split(":") for kv in kv_pairs]))
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
    data = parse(get_data(year=2020, day=4))
    print("\n".join(solve(data)))
