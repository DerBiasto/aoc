"""AoC 13, 2021: Transparent Origami"""
import copy

from aocd import get_data

InputType = tuple[set[tuple[int, int]], list[tuple[str, int]]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    batches = puzzle_input.split("\n\n")
    coords = set()
    for line in batches[0].split("\n"):
        x, y = tuple(map(int, line.split(",")))
        coords.add((x, y))
    folds = [(line[11], int(line[13:])) for line in batches[1].split("\n")]
    return coords, folds


def fold(data: InputType) -> set[tuple[int, int]]:
    coords = data[0]

    for axis, pos in data[1]:
        if axis == "y":
            coords = {(x, y) if y < pos else (x, 2 * pos - y) for x, y in coords}
        else:
            coords = {(x, y) if x < pos else (2 * pos - x, y) for x, y in coords}

    return coords


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return len(fold((data[0], data[1][:1])))


def part2(data: InputType) -> str:
    """Solve part 2."""
    coords = fold(data)

    max_x = max(c[0] for c in coords)
    max_y = max(c[1] for c in coords)
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
