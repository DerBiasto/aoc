"""AoC 14, 2020: Docking Data"""

from aocd import get_data
import parse as p

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    lines = puzzle_input.split("\n")
    mask = p.parse("mask = {}", lines[0]).fixed[0]
    return (mask, [tuple(map(int, p.parse("mem[{}] = {}", line))) for line in lines[1:]])


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
    data = parse(get_data(year=2020, day=14))
    print("\n".join(solve(data)))
