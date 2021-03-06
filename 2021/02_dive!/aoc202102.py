"""AoC 2, 2021: Dive!"""

from aocd import get_data

InputType = list[tuple[str, int]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        (split_line[0], int(split_line[1]))
        for line in puzzle_input.split("\n")
        if (split_line := line.split())
    ]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    x = y = 0
    for command, value in data:
        if command == "forward":
            x += value
        elif command == "down":
            y += value
        elif command == "up":
            y -= value
    return x * y


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    pos = depth = aim = 0
    for command, value in data:
        if command == "forward":
            pos += value
            depth += aim * value
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value
    return pos * depth


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=2))
    print("\n".join(solve(data)))
