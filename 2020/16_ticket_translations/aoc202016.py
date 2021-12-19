"""AoC 16, 2020: Ticket Translations"""
from aocd import get_data
import parse as p

InputType = tuple[dict[str, tuple[int, int, int, int]], tuple[int, ...], list[tuple[int, ...]]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    chunks = puzzle_input.split("\n\n")
    rules = {}
    for line in chunks[0].split("\n"):
        name, *args = p.parse("{}: {}-{} or {}-{}", line).fixed
        rules[name] = tuple(map(int, args))
    return (
        rules,
        tuple(map(int, chunks[1].split("\n", 1)[1].split(","))),
        [tuple(map(int, line.split(","))) for line in chunks[2].split("\n")[1:]],
    )


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    ret = 0
    for ticket in data[2]:
        for num in ticket:
            if not any(
                    a <= num <= b or c <= num <= d
                    for rule, (a, b, c, d) in data[0].items()
            ):
                ret += num
    return ret


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    valid = []
    for ticket in data[2]:
        if all(
                any(
                    a <= num <= b or c <= num <= d
                    for rule, (a, b, c, d) in data[0].items())
                for num in ticket
        ):
            valid.append(ticket)
    possible_positions = {
        name: {i for i in range(len(valid[0])) if all(a <= v[i] <= b or c <= v[i] <= d for v in valid)}
        for name, (a, b, c, d) in data[0].items()
    }

    ret = 1
    used = set()
    for name, possible in sorted(possible_positions.items(), key=lambda item: len(item[1])):
        name: str
        possible: set[int]
        i = (possible - used).pop()
        used.add(i)
        possible.clear()
        possible.add(i)
        if name.startswith("departure") or len(data[0]) < 6:
            ret *= data[1][i]
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
    data = parse(get_data(year=2020, day=16))
    print("\n".join(solve(data)))
