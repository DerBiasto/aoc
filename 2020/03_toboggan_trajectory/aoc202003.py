"""AoC 3, 2020: Toboggan Trajectory"""

from aocd import get_data

InputType = list[list[bool]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        [c == "#" for c in line]
        for line in puzzle_input.split("\n")
    ]


def count_trees(dx: int, dy: int, data: InputType) -> int:
    x = y = trees = 0
    n = len(data[0])
    while y < len(data):
        trees += data[y][x]
        x = (x + dx) % n
        y = y + dy
    return trees


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return count_trees(3, 1, data)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    ret = 1
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        ret *= count_trees(dx, dy, data)
    return ret


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=3))
    print("\n".join(solve(data)))
