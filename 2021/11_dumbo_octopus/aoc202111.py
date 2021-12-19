"""AoC 11, 2021: Dumbo Octopus"""
import copy
import itertools

from aocd import get_data

InputType = list[list[int]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        list(map(int, line))
        for line in puzzle_input.split("\n")
    ]


def neighbours(x: int, y: int) -> list[tuple[int, int]]:
    ret = []
    for dx, dy in itertools.product(range(-1, 2), repeat=2):
        x_ = x + dx
        y_ = y + dy
        if 0 <= x_ < 10 and 0 <= y_ < 10 and (x_, y_) != (x, y):
            ret.append((x_, y_))
    return ret


def update(data: InputType) -> OutputType:
    q = []
    flashes = set()
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            row[x] += 1
            if row[x] >= 10:
                q.append((x, y))

    for x, y in q:
        if data[y][x] >= 10 and (x, y) not in flashes:
            flashes.add((x, y))
            for x_, y_ in neighbours(x, y):
                if (x_, y_) in flashes:
                    continue
                data[y_][x_] += 1
                if data[y_][x_] >= 10:
                    q.append((x_, y_))

    for x, y in flashes:
        data[y][x] = 0

    return len(flashes)


def print_grid(data: InputType) -> str:
    print("\n".join("".join(str(v) if v < 10 else "x" for v in row) for row in data))
    print()


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    data = copy.deepcopy(data)
    return sum(update(data) for _ in range(100))


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    n = 1
    while True:
        if update(data) == 100:
            return n
        n += 1


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=11))
    print("\n".join(solve(data)))
