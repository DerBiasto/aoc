"""AoC 19, 2021: BEacon Scanner"""
import copy
from typing import Iterator

from aocd import get_data


Coord = tuple[int, int, int]
InputType = dict[int, set[Coord]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return {
        i: {
            tuple(map(int, line.split(",")))
            for line in batch.split("\n")[1:]
        }
        for i, batch in enumerate(puzzle_input.split("\n\n"))
    }


def get_rotations(diffs: set[Coord]) -> Iterator[set[Coord]]:
    rotations = [
        lambda x, y, z: (x, y, z),
        lambda x, y, z: (x, z, -y),
        lambda x, y, z: (x, -y, -z),
        lambda x, y, z: (x, -z, y),
        lambda x, y, z: (-x, -y, z),
        lambda x, y, z: (-x, z, y),
        lambda x, y, z: (-x, y, -z),
        lambda x, y, z: (-x, -z, -y),
        lambda x, y, z: (y, x, -z),
        lambda x, y, z: (y, -z, -x),
        lambda x, y, z: (y, -x, z),
        lambda x, y, z: (y, z, x),
        lambda x, y, z: (-y, x, z),
        lambda x, y, z: (-y, z, -x),
        lambda x, y, z: (-y, -x, -z),
        lambda x, y, z: (-y, -z, x),
        lambda x, y, z: (z, y, -x),
        lambda x, y, z: (z, -x, -y),
        lambda x, y, z: (z, -y, x),
        lambda x, y, z: (z, x, -y),
        lambda x, y, z: (-z, y, x),
        lambda x, y, z: (-z, x, -y),
        lambda x, y, z: (-z, -y, -x),
        lambda x, y, z: (-z, -x, y),
    ]
    for rotator in rotations:
        yield set(rotator(x, y, z) for x, y, z in diffs)


def get_position(scanner: int, diffs: dict[int, dict[Coord, set[Coord]]]) -> Coord:
    for a, a_diffs in diffs[scanner].items():
        for b, base_diffs in diffs[0].items():
            if any(len(rotated_a_diffs.intersection(base_diffs)) >= 12 for rotated_a_diffs in get_rotations(a_diffs)):
                return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return None
    scanners = {
        0: (0, 0, 0)
    }
    diffs: dict[int, dict[Coord, set[Coord]]] = {}
    for scanner, beacons in data.items():
        diffs[scanner] = {}
        for a in beacons:
            if a not in diffs[scanner]:
                diffs[scanner][a] = set()
            for b in beacons:
                diffs[scanner][a].add((a[0] - b[0], a[1] - b[1], a[2] - b[2]))
    q = list(diffs.keys())
    for scanner in q:
        if scanner == 0:
            continue
        print(scanner)
        scanner_position = get_position(scanner, diffs)
        if scanner_position is None:
            q.append(scanner)
            continue
        scanners[scanner] = scanner_position
        for b in diffs[scanner]:
            abs_position = tuple(x + y for x, y in zip(scanner_position, b))
            if abs_position in diffs[0]:
                continue
            update = {
                abs_position: {
                    tuple(x - y for x, y in zip(abs_position, a))
                    for a in diffs[0]
                }
            }
            update2 = {
                a: {
                    tuple(x - y for x, y in zip(a, abs_position))
                }
                for a in diffs[0]
            }
            diffs[0].update(update)
            diffs[0].update(update2)
    return len(diffs[0])


def part2(data: InputType) -> OutputType:
    """Solve part 2."""


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=19))
    print("\n".join(solve(data)))
