"""AoC 8, 2021: Seven Segment Search"""

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    lines = puzzle_input.split("\n")

    ret = []
    for line in lines:
        sort = lambda lst: sorted(("".join(sorted(d)) for d in lst.strip().split(" ")), key=lambda s: (len(s), s))
        digits, values = line.split("|", 1)
        ret.append((sort(digits), ["".join(sorted(d)) for d in values.strip().split(" ")]))
    return ret


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    ret = 0
    for digits, values in data:
        code = {}
        code[digits[0]] = 1
        code[digits[1]] = 7
        code[digits[2]] = 4
        code[digits[-1]] = 8
        s = 0
        for v in values:
            if v in code:
                s += 1
        ret += s
    return ret


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    ret = 0
    for digits, values in data:
        code = {}
        code[digits[0]] = 1
        code[digits[1]] = 7
        code[digits[2]] = 4
        code[digits[9]] = 8

        five_segments = [set(x) for x in digits[3:6]]
        six_segments = [set(x) for x in digits[6:9]]

        adg = set.intersection(*five_segments)
        be = set(digits[9]) - adg - set(digits[0])

        nine = set().union(*[x for x in six_segments if not be <= x])
        zero = set().union(*[x for x in six_segments if not adg <= x])
        six = set().union(*[x for x in six_segments if be <= x and adg <= x])

        three = set().union(*[x for x in five_segments if not be & x])
        five = set().union(*[x for x in five_segments if be & x and x <= nine])
        two = set().union(*[x for x in five_segments if not x <= nine])

        code["".join(sorted(nine))] = 9
        code["".join(sorted(zero))] = 0
        code["".join(sorted(six))] = 6
        code["".join(sorted(three))] = 3
        code["".join(sorted(five))] = 5
        code["".join(sorted(two))] = 2

        for i, v in enumerate(reversed(values)):
            ret += code[v] * 10 ** i
    return ret


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=8))
    print("\n".join(solve(data)))
