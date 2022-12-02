"""AoC 1, 2022: Calorie Counting."""
import copy
from typing import Iterator

from aocd import get_data

InputType = list[list[int]]
OutputType = int


def parse_data(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        [
            int(line)
            for line in batch.split("\n")
        ]
        for batch in puzzle_input.split("\n\n")
    ]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return max(sum(batch) for batch in data)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    return sum(sorted(sum(batch) for batch in data)[-3:])


def solve(data: InputType) -> Iterator[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    yield str(solution1)
    if solution2 is not None:
        yield str(solution2)


if __name__ == "__main__":
    data = parse_data(get_data(year=2022, day=1))
    print("\n".join(solve(data)))
