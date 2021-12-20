"""AoC 20, 2021: Trench Map"""
import copy

from aocd import get_data

InputType = dict
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    batches = puzzle_input.split("\n\n")
    lines = batches[1].split("\n")
    algo = batches[0]
    return {
        "algo": algo,
        "default": False,
        "data": {
            (x, y): c == "#"
            for y, line in enumerate(lines)
            for x, c in enumerate(line)
        },
        "miny": 0,
        "maxy": len(lines) + 1,
        "minx": 0,
        "maxx": len(lines[0]) + 1,
    }


def get_new_value(x, y, data) -> bool:
    val = "".join("1" if data["data"].get((x + dx, y + dy), data["default"]) else "0"
                  for dy in (-1, 0, 1) for dx in (-1, 0, 1))
    return data["algo"][int(val, base=2)] == "#"


def update(data: InputType) -> None:
    data["miny"] -= 1
    data["maxy"] += 1
    data["minx"] -= 1
    data["maxx"] += 1
    data["data"] = {
        (x, y): get_new_value(x, y, data)
        for y in range(data["miny"], data["maxy"])
        for x in range(data["minx"], data["maxx"])
    }
    data["default"] = get_new_value(1j, 1j, data)


def print_grid(data):
    print()
    print("\n".join(
        "".join("#" if data["data"].get((x, y), data["default"]) else "."
                for x in range(data["minx"] - 3, data["maxx"] + 3))
        for y in range(data["miny"] - 3, data["maxy"] + 3)))
    print()


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    update(data)
    update(data)
    print_grid(data)
    return len([v for v in data["data"].values() if v])


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    for _ in range(50):
        update(data)
    print_grid(data)
    return len([v for v in data["data"].values() if v])


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=20))
    print("\n".join(solve(data)))
