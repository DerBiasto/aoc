"""AoC 17, 2021: Trick Shot"""
import copy

from aocd import get_data

InputType = tuple[tuple[int, int], tuple[int, int]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    parts = puzzle_input.removeprefix("target area: ").split(", ")
    return tuple(map(int, parts[0][2:].split(".."))), tuple(map(int, parts[1][2:].split("..")))


def update(x: int, y: int, dx: int, dy: int) -> tuple[int, int, int, int]:
    return (x + dx, y + dy, dx - 1 if dx > 0 else dx + 1 if dx < 0 else 0, y - 1)


def hit(x: int, y: int, dx: int, dy: int, target: InputType) -> bool:
    (minx, maxx), (miny, maxy) = target
    while x <= maxx:
        x, y, dx, dy = update(x, y, dx, dy)
        if minx <= x <= maxx and miny <= y <= maxy:
            return True


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    x_target = set(range(data[0][0], data[0][1] + 1))
    y_target = set(range(data[1][0], data[1][1] + 1))
    x_positions = {
        x: set(i * x - (i * (i + 1) // 2) for i in range(0, x))
        for x in range(data[0][1], 0, -1)
    }
    y_positions = {
        y: set(i * y - (i * (i + 1) // 2) for i in range(0, data[0][1]))
        for y in range(data[0][1], 0, -1)
    }
    for x, x_pos in x_positions.items():
        if not x_pos & x_target:
            continue
        for y, y_pos in y_positions.items():
            if not y_pos & y_target:
                continue
            return max(y_pos)


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    x_target = set(range(data[0][0], data[0][1] + 1))
    y_target = set(range(data[1][0], data[1][1] + 1))
    x_positions = {
        x: lst
        for x in range(data[0][1] + 1)
        if set(lst := list(i * x - (i * (i - 1) // 2) for i in range(0, x + 1))) & x_target
    }
    y_positions = {
        y: lst
        for y in range(data[1][0], data[0][1])
        if set(lst := list(i * y - (i * (i - 1) // 2) for i in range(0, data[0][1]))) & y_target
    }
    ret = set()
    for y, y_pos in y_positions.items():
        for i, v in enumerate(y_pos):
            if v in y_target:
                for x, x_pos in x_positions.items():
                    if x_pos[i if i < len(x_pos) else -1] in x_target:
                        ret.add((x, y))
    return len(ret)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=17))
    print("\n".join(solve(data)))
