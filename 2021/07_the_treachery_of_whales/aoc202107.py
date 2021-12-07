"""AoC 7, 2021: The Treachery of Whales"""
import statistics

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return list(map(int, puzzle_input.split(",")))


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    median = statistics.median(data)
    return int(sum(abs(x - median) for x in data))


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    data.sort()
    vals = []
    for i in range(data[0], data[-1] + 1):
        vals.append(int(sum(abs(x - i) * (abs(x - i) + 1) for x in data)) // 2)
    return min(vals)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=7))
    print("\n".join(solve(data)))
