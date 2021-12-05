"""AoC 4, 2021: Giant Squid"""

from aocd import get_data


class BoardEntry:
    def __init__(self, num: int, drawn: bool = False):
        self.num = num
        self.drawn = drawn

    def draw_number(self, num: int) -> bool:
        if num == self.num:
            self.drawn = True
        return self.drawn

    def __bool__(self) -> bool:
        return self.drawn


class Board:
    n = 5

    def __init__(self, board_input: str):
        self._board = {
            (i, j): Board(num)
            for i, line in enumerate(board_input.split("\n"))
            for j, num in enumerate(line.split(" "))
        }
        assert len(self._board) == self.n ** 2

    def draw_number(self, num) -> None:
        for entry in self._board.values():
            entry.draw_number(num)

    def is_won(self) -> bool:
        return any(
            # Either all numbers in one row…
            all(self._board[(i, j)] for j in range(self.n))
            # or in one column have been drawn.
            or all(self._board[(j, i)] for j in range(self.n))
            for i in range(self.n)
        )

    def score(self, num: int) -> int:
        return num * sum(entry.num for entry in self._board if not entry)


InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    chunks = puzzle_input.split("\n\n")

    draw_order = chunks[0].split(",")

    boards = [Board(board_input) for board_input in chunks[1:]]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""


def part2(data: InputType) -> OutputType:
    """Solve part 2."""


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=4))
    print("\n".join(solve(data)))
