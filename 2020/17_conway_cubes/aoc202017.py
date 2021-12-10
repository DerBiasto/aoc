"""AoC 17, 2020: Conway Cubes"""
import copy
import dataclasses
from collections import defaultdict

from aocd import get_data

InputType = dict[int, dict[int, dict[int, dict[int, "Cube"]]]]
OutputType = int


@dataclasses.dataclass
class Cube:
    state: bool
    count: int = 0


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    ret = {}
    ret.update({
        0: {
            0: {
                x: {
                    w: Cube(c == "#")
                    for w, c in enumerate(line)
                }
                for x, line in enumerate(puzzle_input.split("\n"))
            }
        }
    })
    return ret


def update(data: InputType, part2: bool = False) -> None:
    if part2:
        minw, maxw = min(data), max(data)
    else:
        minw, maxw = 1, -1
    minz, maxz = min(data[0]), max(data[0])
    miny, maxy = min(data[0][0]), max(data[0][0])
    minx, maxx = min(data[0][0][0]), max(data[0][0][0])
    for w in range(minw - 1, maxw + 2):
        if w not in data:
            data[w] = {}
        for z in range(minz - 1, maxz + 2):
            if z not in data[w]:
                data[w][z] = {}
            for y in range(miny - 1, maxy + 2):
                if y not in data[w][z]:
                    data[w][z][y] = {}
                for x in range(minx - 1, maxx + 2):
                    if x not in data[w][z][y]:
                        data[w][z][y][x] = Cube(False)
                    cube = data[w][z][y][x]
                    for w_ in (w - 1, w, w + 1):
                        if w_ not in data:
                            continue
                        for z_ in (z - 1, z, z + 1):
                            if z_ not in data[w_]:
                                continue
                            for y_ in (y - 1, y, y + 1):
                                if y_ not in data[w_][z_]:
                                    continue
                                for x_ in (x - 1, x, x + 1):
                                    if x_ not in data[w_][z_][y_]:
                                        continue
                                    if (w_, z_, y_, x_) == (w, z, y, x):
                                        continue
                                    if data[w_][z_][y_][x_].state:
                                        cube.count += 1

    for cube_ in data.values():
        for layer in cube_.values():
            for row in layer.values():
                for cube in row.values():
                    if cube.state:
                        if not 2 <= cube.count <= 3:
                            cube.state = False
                    else:
                        if cube.count == 3:
                            cube.state = True
                    cube.count = 0


def print_matrix(data: InputType) -> None:
    for w, cube in sorted(data.items()):
        for z, layer in sorted(cube.items()):
            print(f"Layer {z=} {w=}")
            for _, row in sorted(layer.items()):
                print("".join("#" if cube.state else "." for _, cube in sorted(row.items())))
            print()


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    data = copy.deepcopy(data)
    for _ in range(6):
        update(data)
    return sum(c.state for cube in data.values() for layer in cube.values() for row in layer.values() for c in row.values())


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    for _ in range(6):
        update(data, part2=True)
    return sum(c.state for cube in data.values() for layer in cube.values() for row in layer.values() for c in row.values())


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=17))
    print("\n".join(solve(data)))
