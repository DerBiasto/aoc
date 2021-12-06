"""AoC 16, 2020: Ticket Translations"""

from aocd import get_data
import parse as p

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    chunks = puzzle_input.split("\n\n")
    rules = {}
    for line in chunks[0].split("\n"):
        name, *args = p.parse("{}: {}-{} or {}-{}", line).fixed
        rules[name] = tuple(map(int, args))
    return (
        rules,
        tuple(map(int, chunks[1].split("\n", 1)[1].split(","))),
        [tuple(map(int, line.split(","))) for line in chunks[2].split("\n")[1:]],
    )


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
    data = parse(get_data(year=2020, day=16))
    print("\n".join(solve(data)))
