"""AoC 15, 2020: Rambunctious Recitation"""

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return list(map(int, puzzle_input.split(",")))


def speak(data: InputType, num: int) -> OutputType:
    age = dict((n, i) for i, n in enumerate(data[:-1]))
    prev = data[-1]
    for i in range(len(data), num):
        a = age.get(prev)
        age[prev] = i - 1
        if a is None:
            prev = 0
        else:
            prev = i - 1 - a
    return prev


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return speak(data, 2020)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    return speak(data, 30000000)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=15))
    print("\n".join(solve(data)))
