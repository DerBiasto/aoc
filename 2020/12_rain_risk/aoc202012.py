"""AoC 12, 2020: Rain Risk"""

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        (line[0], int(line[1:]))
        for line in puzzle_input.split("\n")
    ]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    x = y = orientation = 0
    for op, val in data:
        if op == "E":
            x += val
        elif op == "W":
            x -= val
        elif op == "N":
            y += val
        elif op == "S":
            y -= val
        elif op == "L":
            orientation += val // 90
        elif op == "R":
            orientation -= val // 90
        elif op == "F":
            if orientation == 0:
                x += val
            elif orientation == 1:
                y += val
            elif orientation == 2:
                x -= val
            elif orientation == 3:
                y -= val
        orientation %= 4
    return abs(x) + abs(y)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    ship_x = ship_y = 0
    x, y = 10, 1
    for op, val in data:
        if op == "E":
            x += val
        elif op == "W":
            x -= val
        elif op == "N":
            y += val
        elif op == "S":
            y -= val
        elif op == "L" or op == "R":
            if op == "R":
                val *= -1
            val = (val // 90) % 4
            if val == 0:
                pass
            elif val == 1:
                x, y = -y, x
            elif val == 2:
                x, y = -x, -y
            elif val == 3:
                x, y = y, -x
        elif op == "F":
            ship_x += val * x
            ship_y += val * y
    return abs(ship_x) + abs(ship_y)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=12))
    print("\n".join(solve(data)))
