"""AoC 1, 2021: Sonar"""

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return list(map(int, puzzle_input.split("\n")))


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return sum(
        1
        for i, depth in enumerate(data[:-1])
        if depth < data[i + 1]
    )


def part2_old(data: InputType) -> OutputType:
    """Solve part 2."""
    def sum_group(index: int) -> int:
        return sum(data[i] for i in range(index, index + 3))
    return sum(
        1
        for i in range(len(data) - 3)
        if sum_group(i) < sum_group(i + 1)
    )


def part2(data: InputType) -> OutputType:
    """Solve part 2 more efficiently."""
    return sum(
        1
        for i, depth in enumerate(data[:-3])
        if depth < data[i + 3]
    )


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=1))
    print("\n".join(solve(data)))
