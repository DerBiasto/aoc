"""AoC 6, 2020: Custom Customs"""

from aocd import get_data

InputType = list[list[set[str]]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        list(map(set, batch.split("\n")))
        for batch in puzzle_input.split("\n\n")
    ]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return sum(len(set.union(*group)) for group in data)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    return sum(len(set.intersection(*group)) for group in data)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=6))
    print("\n".join(solve(data)))
