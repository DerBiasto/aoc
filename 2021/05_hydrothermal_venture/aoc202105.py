"""AoC 5, 2021: Hydrothermal Venture"""

from collections import Counter
from typing import NamedTuple

from aocd import get_data

Pos = NamedTuple("Pos", [("x", int), ("y", int)])


class Line:
    def __init__(self, line_input: str):
        start_input, end_input = tuple(line_input.split(" -> ", 1))
        self.start = Pos(*map(int, start_input.split(",", 1)))
        self.end = Pos(*map(int, end_input.split(",", 1)))

    def get_fields(self, diagonal: bool) -> list[Pos]:
        x_step = 1 if self.start.x <= self.end.x else -1
        y_step = 1 if self.start.y <= self.end.y else -1
        if self.start.x == self.end.x:
            return [Pos(self.start.x, y) for y in range(self.start.y, self.end.y + y_step, y_step)]
        if self.start.y == self.end.y:
            return [Pos(x, self.start.y) for x in range(self.start.x, self.end.x + x_step, x_step)]
        if diagonal:
            return [Pos(x, y) for x, y in zip(range(self.start.x, self.end.x + x_step, x_step),
                                              range(self.start.y, self.end.y + y_step, y_step))]
        return []


InputType = list[Line]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        Line(line)
        for line in puzzle_input.split("\n")
    ]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    grid = Counter()
    for line in data:
        grid.update(line.get_fields(diagonal=False))

    return sum(1 for v in grid.values() if v >= 2)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    grid = Counter()
    for line in data:
        grid.update(line.get_fields(diagonal=True))

    return sum(1 for v in grid.values() if v >= 2)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=5))
    print("\n".join(solve(data)))
