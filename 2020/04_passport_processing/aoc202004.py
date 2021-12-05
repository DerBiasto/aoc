"""AoC 4, 2020: Passport Processing"""

from aocd import get_data

InputType = list[dict[str, str]]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    ret = []
    for passport in puzzle_input.split("\n\n"):
        kv_pairs = passport.split()
        ret.append(dict([kv.split(":") for kv in kv_pairs]))
    return ret


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    valid_keys = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}
    return len([p for p in data if valid_keys <= p.keys()])


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    ret = 0
    for p in data:
        try:
            if not (1920 <= int(p["byr"]) <= 2002):
                continue
            if not (2010 <= int(p["iyr"]) <= 2020):
                continue
            if not (2020 <= int(p["eyr"]) <= 2030):
                continue
            if p["hgt"].endswith("cm"):
                if not (150 <= int(p["hgt"].removesuffix("cm")) <= 193):
                    continue
            elif p["hgt"].endswith("in"):
                if not (59 <= int(p["hgt"].removesuffix("in")) <= 76):
                    continue
            else:
                continue
            if not p["hcl"].startswith("#") or len(p["hcl"]) != 7:
                continue
            try:
                int(p["hcl"].removeprefix("#"), base=16)
            except ValueError:
                continue
            if p["ecl"] not in set("amb blu brn gry grn hzl oth".split()):
                continue
            if len(p["pid"]) != 9:
                continue
            try:
                int(p["pid"])
            except ValueError:
                continue
        except KeyError:
            continue
        ret += 1
    return ret


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(data)
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2020, day=4))
    print("\n".join(solve(data)))
