"""AoC 14, 2020: Docking Data"""
from collections import defaultdict

import parse as p
from aocd import get_data

InputType = list[tuple[int, str]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    ret = []
    for line in puzzle_input.split("\n"):
        if result := p.parse("mask = {}", line):
            ret.append((-1, result.fixed[0]))
        else:
            ret.append(tuple(map(int, p.parse("mem[{}] = {}", line))))
    return ret


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    mask_and = mask_or = None
    mem = defaultdict(int)
    for pos, val in data:
        if pos < 0:
            mask_and = int("".join("0" if c == "0" else "1" for c in val), base=2)
            mask_or = int("".join("1" if c == "1" else "0" for c in val), base=2)
        else:
            mem[pos] = val & mask_and | mask_or
    return sum(mem.values())


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    mask = ""
    mem = defaultdict(int)
    for pos, val in data:
        if pos < 0:
            mask = val
        else:
            p = list("{:0>36b}".format(pos))
            for i, x in enumerate(mask):
                if x == "0":
                    continue
                p[i] = x
            q = ["".join(p)]
            for x in q:
                if (i := x.find("X")) >= 0:
                    q.append(x[:i] + "0" + x[i + 1:])
                    q.append(x[:i] + "1" + x[i + 1:])
                else:
                    mem[x] = val
    return sum(mem.values())


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=14))
    print("\n".join(solve(data)))
