"""AoC 8, 2020: Handheld Halting"""

from aocd import get_data

InputType = list[tuple[str, int]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return [
        (line.split()[0], int(line.split()[1]))
        for line in puzzle_input.split("\n")
    ]


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    pointer = acc = 0
    executed = set()
    while cmd := data[pointer]:
        if pointer in executed:
            return acc
        executed.add(pointer)
        op, val = cmd
        if op == "acc":
            acc += val
            pointer += 1
        elif op == "nop":
            pointer += 1
        elif op == "jmp":
            pointer += val


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    potentially_corrupted_cmds = []

    def execute(data: InputType, corrupted: int = -1) -> int:
        pointer = acc = 0
        executed = set()
        end = len(data)
        while cmd := data[pointer]:
            if pointer in executed:
                raise RuntimeError
            executed.add(pointer)
            op, val = cmd
            if op == "acc":
                acc += val
                pointer += 1
            elif op == "nop":
                if pointer == corrupted:
                    pointer += val
                else:
                    if corrupted < 0:
                        potentially_corrupted_cmds.append(pointer)
                    pointer += 1
            elif op == "jmp":
                if pointer == corrupted:
                    pointer += 1
                else:
                    if corrupted < 0:
                        potentially_corrupted_cmds.append(pointer)
                    pointer += val
            if pointer == end:
                return acc

    # Gather data on potentially corrupted commands.
    try:
        execute(data)
    except RuntimeError:
        pass

    for x in reversed(potentially_corrupted_cmds):
        try:
            return execute(data, x)
        except RuntimeError:
            pass


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=8))
    print("\n".join(solve(data)))
