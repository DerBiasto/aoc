"""AoC 16, 2021: Packet Decoder"""
import copy

from aocd import get_data

InputType = list[int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    ret = []
    for line in puzzle_input.split("\n"):
        x = "{0:b}".format(int(line, base=16))
        while len(x) < 4 * len(line):
            x = "0" + x
        ret.append(x)
    return ret


def peek(data: list[str, int], n: int) -> str:
    s = data[0][:n]
    data[0] = data[0][n:]
    return s


def decode(data: list[str, int]) -> tuple[str, int]:
    version = int(peek(data, 3), 2)
    data[1] += version
    type_ = int(peek(data, 3), base=2)
    if type_ == 4:
        t = []
        while True:
            cont, *val = peek(data, 5)
            t += val
            if cont == "0":
                break
        return int("".join(t), 2)
    else:
        ltype = peek(data, 1)
        values = []
        if ltype == "0":
            # length in bit
            length = int(peek(data, 15), 2)
            data[0], temp = peek(data, length), data[0]
            while data[0]:
                values.append(decode(data))
            data[0] = temp
        else:
            length = int(peek(data, 11), 2)
            for _ in range(length):
                values.append(decode(data))
        if type_ == 0:
            return sum(values)
        if type_ == 1:
            x = 1
            for v in values:
                x *= v
            return x
        if type_ == 2:
            return min(values)
        if type_ == 3:
            return max(values)
        if type_ == 5:
            return values[0] > values[1]
        if type_ == 6:
            return values[0] < values[1]
        if type_ == 7:
            return values[0] == values[1]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    ret = []
    for line in data:
        d = [line, 0]
        decode(d)
        ret.append(d[1])
    return ret


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    ret = []
    for line in data:
        ret.append(decode([line, 0]))
    return ret


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=16))
    print("\n".join(solve(data)))
