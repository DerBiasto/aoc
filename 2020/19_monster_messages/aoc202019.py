"""AoC 19, 2020: Monster Messages"""
import copy
from typing import Iterator

from aocd import get_data

InputType = tuple[dict[str, list[str], list[str]]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    batches = puzzle_input.split("\n\n")
    rules = {}
    for line in batches[0].split("\n"):
        num, rule = tuple(line.split(":"))
        rules[num] = [
            option[1:-1] if option.startswith('"') else option
            for option in map(str.strip, rule.split("|"))
        ]
    messages = [
        line
        for line in batches[1].split("\n")
    ]
    return rules, messages


def match(m: str, data: InputType) -> bool:
    return any(m == "" for m in check_rule(m, "0", data))


def check_rule(s_: str, rule: str, data: InputType) -> Iterator[str]:
    if rule not in data[0]:
        if s_.startswith(rule):
            yield s_[len(rule):]
    else:
        for option in data[0][rule]:
            yield from check_rules(s_, option.split(), data)


def check_rules(s: str, option: list[str], data: InputType) -> Iterator[str]:
    if not option:
        yield s
    else:
        for s in check_rule(s, option[0], data):
            yield from check_rules(s, option[1:], data)


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    return sum(match(m, data) for m in data[1])


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    # data[0]["8"] = [" ".join(["42"] * i) for i in range(1, n)]
    # data[0]["11"] = [" ".join(["42"] * i + ["31"] * i) for i in range(1, n)]
    data[0]["8"] = ["42", "42 8"]
    data[0]["11"] = ["42 31", "42 11 31"]

    return sum(match(m, data) for m in data[1])


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=19))
    print("\n".join(solve(data)))
