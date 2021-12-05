"""AoC 5, 2020: Binary Boarding"""

from aocd import get_data

InputType = list[str]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return puzzle_input.split("\n")


def convert(boarding_pass: str) -> int:
    return int(boarding_pass.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), base=2)


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return max(map(convert, data))


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    sorted_ids = sorted(map(convert, data))[:-1]
    for i, seat in enumerate(sorted_ids):
        if seat + 1 != sorted_ids[i + 1]:
            return seat + 1


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=5))
    print("\n".join(solve(data)))
