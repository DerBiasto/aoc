"""AoC 15, 2021: Chiton"""
import copy
from queue import PriorityQueue

from aocd import get_data

InputType = dict[tuple[int, int], int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return {
        (x, y): int(v)
        for y, line in enumerate(puzzle_input.split("\n"))
        for x, v in enumerate(line)
    }


def neighbours(x: int, y: int) -> list[tuple[int, int]]:
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def find_path(data: InputType) -> OutputType:
    maxx = maxy = int(len(data) ** 0.5)
    q = PriorityQueue()
    q.put((0, (0, 0)))
    checked = {(0, 0): 0}
    while q.not_empty:
        cost, (x, y) = q.get()
        if (x, y) == (maxx - 1, maxy - 1):
            break
        for (a, b) in neighbours(x, y):
            if 0 <= a < maxx and 0 <= b < maxy:
                new_cost = data[(a, b)]
                if cost + new_cost < checked.get((a, b), 10_000_000_000):
                    checked[(a, b)] = cost + new_cost
                    q.put((checked[(a, b)], (a, b)))
    return checked[(maxx - 1, maxy - 1)]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return find_path(data)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    maxx = maxy = int(len(data) ** 0.5)
    data = {
        (x + dx * maxx, y + dy * maxy): (v + dx + dy - 1) % 9 + 1
        for dy in range(5)
        for dx in range(5)
        for (x, y), v in tuple(data.items())
    }
    maxx *= 5
    maxy *= 5
    # print("\n".join("".join(str(data[(x, y)]) for x in range(maxx)) for y in range(maxy)))
    return find_path(data)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=15))
    print("\n".join(solve(data)))
