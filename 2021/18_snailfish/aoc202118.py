"""AoC 18, 2021: Snailfish"""
import copy
from typing import Union, Any, Iterator, Optional

from aocd import get_data

InputType = list["SnailfishNumber"]
OutputType = int

Number = Union[int, "SnailfishNumber"]


class SnailfishNumber:
    def __init__(self, a: Number, b: Number):
        self.a = a
        self.b = b
        self.parent_a: Optional[SnailfishNumber] = None
        self.parent_b: Optional[SnailfishNumber] = None

    def _set_a(self, a: Number) -> None:
        self._a = a
        if isinstance(self.a, SnailfishNumber):
            self.a.parent_a = self

    def _get_a(self) -> Number:
        return self._a

    a = property(_get_a, _set_a)

    def _set_b(self, b: Number) -> None:
        self._b = b
        if isinstance(self.b, SnailfishNumber):
            self.b.parent_b = self

    def _get_b(self) -> Number:
        return self._b

    b = property(_get_b, _set_b)

    def __int__(self):
        return 3 * int(self.a) + 2 * int(self.b)

    @classmethod
    def from_str(cls, s_: str) -> "SnailfishNumber":
        stack = []
        current = []
        s = iter(s_)
        for c in s:
            if c == "[":
                stack.append(current)
                current = []
            elif c == ",":
                pass
            elif c == "]":
                current = stack.pop() + [SnailfishNumber(current[0], current[1])]
            else:
                current.append(int(c))
        return current[-1]

    def __add__(self, other: "SnailfishNumber") -> "SnailfishNumber":
        return reduce(copy.deepcopy(SnailfishNumber(self, other)))

    def __repr__(self) -> str:
        return f"[{self.a},{self.b}]"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, SnailfishNumber):
            return (self.a, self.b) == (other.a, other.b)
        return False

    def __iter__(self) -> Iterator[tuple["SnailfishNumber", int]]:
        yield self, 0
        if isinstance(self.a, SnailfishNumber):
            for sn, n in self.a:
                yield sn, n + 1
        if isinstance(self.b, SnailfishNumber):
            for sn, n in self.b:
                yield sn, n + 1

    def iter(self) -> Iterator["SnailfishNumber"]:
        yield self
        if isinstance(self.a, SnailfishNumber):
            yield from self.a.iter()
        if isinstance(self.b, SnailfishNumber):
            yield from self.b.iter()


def reduce(x: SnailfishNumber) -> SnailfishNumber:
    while True:
        lx = list(x)
        print(x)
        for i, (sn, n) in enumerate(lx):
            if n >= 4:
                prev = nxt = None
                if i > 0:
                    prev = lx[i - 1][0]
                if i + 1 < len(lx):
                    nxt, m = lx[i + 1]
                    print(lx)
                    if m > n:
                        continue
                print(prev, sn, nxt)
                if nxt:
                    nxt.a += sn.b
                if prev:
                    prev.b += sn.a
                if sn.parent_a:
                    sn.parent_a.a = 0
                if sn.parent_b:
                    sn.parent_b.b = 0
                print(prev, sn, nxt)
                break
        else:
            for sn in x.iter():
                if isinstance(sn.a, int) and sn.a >= 10:
                    sn.a = SnailfishNumber(sn.a // 2, (sn.a + 1) // 2)
                elif isinstance(sn.b, int) and sn.b >= 10:
                    sn.b = SnailfishNumber(sn.b // 2, (sn.b + 1) // 2)
                else:
                    continue
                break
            else:
                break
    return x


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        SnailfishNumber.from_str(line)
        for line in puzzle_input.split("\n")
    ]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return 0
    ret = data[0]
    for x in data[1:]:
        ret += x
    return int(ret)


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
    data = parse(get_data(year=2021, day=18))
    print("\n".join(solve(data)))
