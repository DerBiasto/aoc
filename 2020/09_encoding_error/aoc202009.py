"""AoC 9, 2020: Encoding Error"""

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        int(line)
        for line in puzzle_input.split("\n")
    ]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    if len(data) <= 25:
        n = 5
    else:
        n = 25
    preambel = set(data[:n])
    for i, num in enumerate(data[n:]):
        for x in preambel:
            if num - x in preambel:
                break
        else:
            return num
        preambel.remove(data[i])
        preambel.add(num)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    target = part1(data)
    start = end = current = 0
    while True:
        if current < target:
            current += data[end]
            end += 1
        elif current > target:
            current -= data[start]
            start += 1
        else:
            seq = sorted(data[start:end])
            return seq[0] + seq[-1]


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=9))
    print("\n".join(solve(data)))
