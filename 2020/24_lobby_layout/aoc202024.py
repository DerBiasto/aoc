"""AoC 24, 2020: Lobby Layout"""
import itertools

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return puzzle_input.split("\n")


def turn_tiles(data: InputType) -> set[tuple[int, int]]:
    black_tiles = set()
    for line in data:
        a = b = 0
        directions = iter(line)
        for c in directions:
            if c == "e":
                a += 1
            elif c == "w":
                a -= 1
            elif c == "n":
                c = next(directions)
                if c == "e":
                    a += 1
                    b += 1
                else:
                    b += 1
            else:
                c = next(directions)
                if c == "e":
                    b -= 1
                else:
                    a -= 1
                    b -= 1
        black_tiles.symmetric_difference_update({(a, b)})
    return black_tiles


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return len(turn_tiles(data))


def get_neighbours(a: int, b: int) -> list[tuple[int, int]]:
    return [
        (a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1), (a + 1, b + 1), (a - 1, b - 1)
    ]


def update_tiles(tiles: set[tuple[int, int]]) -> set[tuple[int, int]]:
    s = sorted(sum(tiles, start=()))
    min_, *_, max_ = s
    # print(s, min_, max_)

    ret = set()
    for a, b in itertools.product(range(min_ - 1, max_ + 2), repeat=2):
        n = len(list(filter(lambda x: x in tiles, get_neighbours(a, b))))
        # print(a, b, n)
        if (a, b) in tiles:
            if 1 <= n <= 2:
                ret.add((a, b))
        else:
            if n == 2:
                ret.add((a, b))
    return ret


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    tiles = turn_tiles(data)
    for _ in range(100):
        tiles = update_tiles(tiles)
    return len(tiles)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=24))
    print("\n".join(solve(data)))
