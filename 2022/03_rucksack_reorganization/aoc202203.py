"""AoC 3, 2022: Rucksack Reorganization."""
import copy
from typing import Iterator

from aocd import get_data

InputType = list[str]
OutputType = int


def parse_data(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        line
        for line in puzzle_input.split("\n")
    ]


def get_score(s: str) -> int:
    if s.islower():
        return ord(s) - ord('a') + 1
    else:
        return ord(s) - ord('A') + 27


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return sum(
        get_score(x)
        for line in data
        for x in set(line[:len(line) // 2]) & set(line[len(line) // 2:])
    )


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    n = 3
    return sum(
        get_score(x)
        for i in range(0, len(data), n)
        for x in set(data[i]).intersection(*[set(data[j]) for j in range(i + 1, i + n)])
    )


def solve(data: InputType) -> Iterator[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    yield str(solution1)
    if solution2 is not None:
        yield str(solution2)


if __name__ == "__main__":
    data = parse_data(get_data(year=2022, day=3))
    print("\n".join(solve(data)))
