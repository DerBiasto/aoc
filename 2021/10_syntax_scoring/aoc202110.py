"""AoC 10, 2021: Syntax Scoring"""
import statistics

from aocd import get_data

InputType = list[str]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return puzzle_input.split("\n")


INVERSE = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
PART1_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
PART2_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    score = 0
    for line in data:
        stack = []
        for c in line:
            if d := INVERSE.get(c):
                stack.append(d)
            elif stack[-1] == c:
                stack.pop(-1)
            else:
                score += PART1_SCORES[c]
                break
    return score


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    scores = []
    for line in data:
        stack = []
        for c in line:
            if d := INVERSE.get(c):
                stack.append(d)
            elif stack[-1] == c:
                stack.pop(-1)
            else:
                break
        else:
            score = 0
            for c in reversed(stack):
                score = score * 5 + PART2_SCORES[c]
            scores.append(score)
    return statistics.median(scores)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=10))
    print("\n".join(solve(data)))
