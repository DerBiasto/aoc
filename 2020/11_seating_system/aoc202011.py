"""AoC 11, 2020: Seating System"""
import copy
import itertools

from aocd import get_data


class Grid:
    occupied = "#"
    empty = "L"
    floor = "."

    def __init__(self, grid: list[list[str]]):
        self._grid = grid
        self.n = len(grid)
        self.m = len(grid[0])

    def __getitem__(self, key: int) -> list[str]:
        return self._grid[key]

    def num_neighbours(self, x: int, y: int, part2: bool) -> int:
        ret = 0
        if not part2:
            for x, y in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1),
                         (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]:
                if 0 <= x < self.n and 0 <= y < self.m:
                    ret += self._grid[x][y] == self.occupied
        else:
            for dx, dy in itertools.product((-1, 0, 1), repeat=2):
                x_ = x
                y_ = y
                if dx == dy == 0:
                    continue
                while True:
                    if 0 <= x_ + dx < self.n and 0 <= y_ + dy < self.m:
                        x_ += dx
                        y_ += dy
                        if self[x_][y_] == self.occupied:
                            ret += 1
                            break
                        elif self[x_][y_] == self.empty:
                            break
                    else:
                        break
        return ret

    def update(self, part2: bool) -> int:
        ret = 0
        new_grid = []
        for x in range(self.n):
            new_grid.append([''] * self.m)
            for y in range(self.m):
                new_grid[x][y] = self[x][y]
                if self[x][y] == self.empty:
                    if not self.num_neighbours(x, y, part2):
                        new_grid[x][y] = self.occupied
                        ret += 1
                elif self[x][y] == self.occupied:
                    if self.num_neighbours(x, y, part2) >= (4 + part2):
                        new_grid[x][y] = self.empty
                        ret += 1
        self._grid = new_grid
        return ret

    def num_occupied(self) -> int:
        return sum(1 for line in self._grid for c in line if c == self.occupied)

    def __str__(self) -> str:
        return "\n".join("".join(line) for line in self._grid)


InputType = Grid
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return Grid([
        list(line)
        for line in puzzle_input.split("\n")
    ])


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    data = copy.deepcopy(data)
    while data.update(part2=False):
        pass
    return data.num_occupied()


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    while data.update(part2=True):
        pass
    return data.num_occupied()


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=11))
    print("\n".join(solve(data)))
