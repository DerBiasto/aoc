"""AoC 9, 2021: Smoke Basin"""

from aocd import get_data

InputType = list[list[int]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        list(map(int, line))
        for line in puzzle_input.split("\n")
    ]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    ret = 0
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if all(
                    data[y_][x_] > val for y_, x_ in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
                    if 0 <= y_ < len(data) and 0 <= x_ < len(data[y_])
            ):
                # print(x, y, val)
                ret += val + 1
    return ret


def measure_basin(x: int, y: int, data: InputType, checked: set[OutputType]) -> OutputType:
    ret = 1
    checked.add((x, y))
    q = [(x + 1, y), (x, y + 1)]
    for x, y in q:
        if (x, y) in checked:
            continue
        checked.add((x, y))
        if not 0 <= y < len(data) or not 0 <= x < len(data[y]):
            continue
        if data[y][x] == 9:
            continue
        ret += 1
        q.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])
    return ret


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    basin_sizes = []
    checked = set()
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if (x, y) in checked:
                continue
            checked.add((x, y))
            if val == 9:
                continue
            basin_sizes.append(measure_basin(x, y, data, checked))
    basin_sizes.sort()
    return basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=9))
    print("\n".join(solve(data)))
