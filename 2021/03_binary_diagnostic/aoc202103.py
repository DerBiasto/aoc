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
    for i in reversed(range(data[0])):
        count0 = count1 = 0
        mask = 1 << i
        for num in data[1]:
            if num & mask:
                count1 += 1
            else:
                count0 += 1
        if count1 >= half_n:
            gamma += 2 ** i
        elif count0 > half_n:
            epsilon += 2 ** i
    return gamma * epsilon


def part2(data: InputType) -> OutputType:
    """Solve part 2."""

    def get_life_support_rating(data: InputType, majority: bool) -> int:
        lifesupport_data = data[1]
        for i in reversed(range(data[0])):
            a, b = [], []
            if len(lifesupport_data) == 1:
                break
            for num in lifesupport_data:
                if (num >> i) & 1:
                    a.append(num)
                else:
                    b.append(num)
                if (len(a) >= len(b)) != majority:
                    lifesupport_data = a
                else:
                    lifesupport_data = b
        return lifesupport_data[0]

    o2 = get_life_support_rating(data, majority=True)
    co2 = get_life_support_rating(data, majority=False)
    return o2 * co2


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
