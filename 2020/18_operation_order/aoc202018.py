"""AoC 18, 2020: Operation Order"""

from aocd import get_data

InputType = list[str, int]
OutputType = int


class Int:
    def __init__(self, val: int):
        self.val = val

    def __mul__(self, other: "Int") -> "Int":
        if isinstance(other, Int):
            return Int(self.val + other.val)
        if isinstance(other, int):
            return Int(self.val + other)
        return NotImplemented

    __add__ = __mul__

    def __sub__(self, other: "Int") -> "Int":
        if isinstance(other, Int):
            return Int(self.val * other.val)
        if isinstance(other, int):
            return Int(self.val * other)
        return NotImplemented

    def __int__(self) -> int:
        return self.val

    def __repr__(self) -> str:
        return f"Int({self.val})"


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        line.replace("(", "( ").replace(")", " )").split() for line in puzzle_input.split("\n")
    ]


def grouping_stack(data: InputType, part2: bool = False) -> int:
    """Calculate intermediate values for subgroups and the final reduced group."""
    stack, current = [], []
    for v in data:
        if v == "(":
            # New subgroup. Push the current group to the stack.
            stack.append(current)
            current = []
        elif v == ")":
            # End of current subgroup. Calculate value of current subgroup, append result to previous group.
            current = stack.pop() + [arithmetic_stack(current, part2)]
        else:
            # Next entry for current group. Can be int or operator, so don't convert here.
            current.append(v)
    # Calculate value for final group.
    return arithmetic_stack(current, part2)


def arithmetic_stack(data: InputType, part2: bool = False) -> int:
    if part2:
        # part 2: + has priority over *
        # Split input into groups of additions to be multiplied together.
        stack, current = [], []
        for v in data:
            if v == "*":
                # New addition group. Push previous group to stack.
                current = stack.append(current) or []
            elif v != "+":
                # New entry for current group. Convert to int.
                current.append(int(v))
        # Sum all addition groups and multiply them together.
        ret = sum(current)
        while stack:
            ret *= sum(stack.pop())
        return ret

    # part 1: + and * have equal priority.
    ret = 0
    data_iter = iter(data)
    for v in data_iter:
        if v == "*":
            ret *= int(next(data_iter))
        elif v == "+":
            ret += int(next(data_iter))
        else:
            ret = int(v)
    return ret


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return sum(grouping_stack(line) for line in data)
    # ret = 0
    # for line in data:
    #     s = "".join(f"Int({token})" if token not in "()+*" else token for token in line).replace("*", "-")
    #     x = eval(s)
    #     ret += int(x)
    # return ret


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    return sum(grouping_stack(line, part2=True) for line in data)
    # ret = 0
    # for line in data:
    #     s = "".join(f"Int({token})" if token not in "()+*" else token for token in line).replace("*", "-").replace("+", "*")
    #     x = eval(s)
    #     ret += int(x)
    # return ret


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=18))
    print("\n".join(solve(data)))
