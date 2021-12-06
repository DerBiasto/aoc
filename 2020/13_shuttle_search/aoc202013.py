"""AoC 13, 2020: Shuttle Search"""
import math

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    lines = puzzle_input.split("\n")
    return (int(lines[0]), [int(x) if x != "x" else 0 for x in lines[1].split(",")])


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    x = data[0]
    wait_times = [(bus - (x % bus), bus) for bus in data[1] if bus]
    min_bus = min(wait_times)
    return min_bus[0] * min_bus[1]


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    remainders = dict((b, (b - i) % b) for i, b in enumerate(data[1]) if b)
    rem_list = list(remainders.items())
    prev, x = rem_list[0]
    for val, rem in rem_list[1:]:
        while x % val != rem:
            x += prev
        prev *= val
    return x


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=13))
    print("\n".join(solve(data)))
