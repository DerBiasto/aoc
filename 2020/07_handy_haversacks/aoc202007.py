"""AoC 7, 2020: Handy Haversacks"""

from aocd import get_data

InputType = dict[str, dict[str, int]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    ret = {}
    for line in puzzle_input.split("\n"):
        outer_bag, inner_bags = line.split(" contain ", 1)
        outer_bag: str
        outer_bag = outer_bag.removesuffix("bags").strip()
        ret[outer_bag] = {}
        if inner_bags == "no other bags.":
            continue
        # Cut off "." from the end, split at ",".
        for inner_bag in inner_bags[:-1].split(","):
            inner_bag: str
            num, color = inner_bag.removesuffix("bag").removesuffix("bags").strip().split(" ", 1)
            ret[outer_bag][color] = int(num)

    return ret


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    inverted_data = {}
    for outer, v in data.items():
        for inner, count in v.items():
            inverted_data.setdefault(inner, {})[outer] = count

    ret = set()
    q = list(inverted_data["shiny gold"].keys())
    for color in q:
        if color in ret:
            continue
        ret.add(color)
        q.extend(inverted_data.get(color, {}).keys())
    print(ret)
    return len(ret)


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
    data = parse(get_data(year=2020, day=7))
    print("\n".join(solve(data)))
