"""AoC 3, 2021: Binary Diagnostic"""

from aocd import get_data

InputType = tuple[int, list[int]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    lines = puzzle_input.split("\n")
    return len(lines[0]), [int(line, base=2) for line in lines]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    gamma = epsilon = 0
    half_n = len(data[1]) // 2
    for i in range(data[0]):
        count = sum((num >> i) & 1 for num in data[1])
        if count >= half_n:
            gamma += 2 ** i
        else:
            epsilon += 2 ** i
        if not count:
            break
    return gamma * epsilon


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
    data = parse(get_data(year=2021, day=3))
    print("\n".join(solve(data)))
