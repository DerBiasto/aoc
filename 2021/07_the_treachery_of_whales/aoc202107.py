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
    mean = statistics.mean(data)
    fuel = lambda n: n * (n + 1) // 2
    return min(sum(fuel(abs(x - int(mean))) for x in data),
               sum(fuel(abs(x - int(mean + 1))) for x in data))


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
