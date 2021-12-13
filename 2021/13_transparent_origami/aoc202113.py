"""AoC 13, 2021: Transparent Origami"""
import copy

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    batches = puzzle_input.split("\n\n")
    coords = set()
    for line in batches[0].split("\n"):
        x, y = tuple(map(int, line.split(",")))
        coords.add((x, y))
    folds = [line[11] for line in batches[1].split("\n")]
    return coords, folds


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    coords = data[0]
    max_x = max(c[0] for c in coords)
    max_y = max(c[1] for c in coords)

    for axis in data[1][:1]:
        if axis == "y":
            half_y = max_y // 2
            coords = {(x, y) if y < half_y else (x, max_y - y) for x, y in coords}
            max_y = half_y - 1
        else:
            half_x = max_x // 2
            coords = {(x, y) if x < half_x else (max_x - x, y) for x, y in coords}
            max_x = half_x - 1
    return len(coords)


def part2(data: InputType) -> str:
    """Solve part 2."""
    coords = data[0]
    max_x = max(c[0] for c in coords)
    max_y = max(c[1] for c in coords)

    for axis in data[1]:
        if axis == "y":
            half_y = max_y // 2
            coords = {(x, y) if y < half_y else (x, max_y - y) for x, y in coords}
            max_y = half_y - 1
        else:
            half_x = max_x // 2
            coords = {(x, y) if x < half_x else (max_x - x, y) for x, y in coords}
            max_x = half_x - 1

    return "\n".join("".join(" " if (x, y) not in coords else "#" for x in range(max_x + 1)) for y in range(max_y + 1))


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=13))
    print("\n".join(solve(data)))
