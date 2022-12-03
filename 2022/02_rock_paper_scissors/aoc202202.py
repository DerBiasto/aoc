"""AoC 2, 2022: Rock Paper Scissors."""
import copy
from typing import Iterator

from aocd import get_data

InputType = list[tuple[int, int]]
OutputType = int


object_map = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def parse_data(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        tuple(object_map[x] for x in line.split())  # type: ignore[misc]
        for line in puzzle_input.split("\n")
    ]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    score = 0
    for enemy, me in data:
        score += me
        if enemy == me:
            score += 3
        elif (me - enemy) % 3 == 1:
            score += 6

    return score


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    score = 0
    for enemy, result in data:
        if result == 1:
            me = (enemy - 2) % 3 + 1
            score += me
        elif result == 2:
            score += enemy + 3
        else:
            me = enemy % 3 + 1
            score += me + 6
    return score


def solve(data: InputType) -> Iterator[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    yield str(solution1)
    if solution2 is not None:
        yield str(solution2)


if __name__ == "__main__":
    data = parse_data(get_data(year=2022, day=2))
    print("\n".join(solve(data)))
