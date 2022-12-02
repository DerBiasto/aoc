"""AoC 21, 2021: Dirac Dice"""
import copy
import itertools
from collections import Counter, defaultdict
from queue import Queue
from typing import Iterator

from aocd import get_data

InputType = tuple[int, int]
OutputType = int


def parse(puzzle_input: str) -> InputType:
    """Parse file input."""
    return tuple(
        int(line.split(": ")[1])
        for line in puzzle_input.split("\n")
    )


def part1(data: InputType) -> OutputType:
    """Solve part 1."""
    def deterministic_die_factory() -> Iterator[int]:
        while True:
            yield from range(1, 100 + 1)

    deterministic_die = deterministic_die_factory()
    roll = lambda: next(deterministic_die)

    pos_a, pos_b = data
    score_a = score_b = num_rolls = 0
    a_active = True
    while score_a < 1000 and score_b < 1000:
        if a_active:
            pos_a = (pos_a + roll() + roll() + roll() - 1) % 10 + 1
            score_a += pos_a
        else:
            pos_b = (pos_b + roll() + roll() + roll() - 1) % 10 + 1
            score_b += pos_b
        num_rolls += 3
        a_active = not a_active
    return min(score_a, score_b) * num_rolls


def part2(data: InputType) -> OutputType:
    """Solve part 2."""
    possible_increases = Counter([sum(x) for x in itertools.product(range(1, 4), repeat=3)])

    start = (data[0], data[1], 0, 0, True)
    wins_a = wins_b = 0
    q = Queue()
    q.put(start)
    counts = {start: 1}
    while not q.empty():
        data = q.get()
        # print(data)
        num = counts.pop(data)
        for inc, n in possible_increases.items():
            pos_a, pos_b, score_a, score_b, a_active = data
            if a_active:
                pos_a = (pos_a + inc) % 10
                score_a = score_a + pos_a + 1
                if score_a >= 21:
                    wins_a += num * n
                    continue
            else:
                pos_b = (pos_b + inc) % 10
                score_b = score_b + pos_b + 1
                if score_b >= 21:
                    wins_b += num * n
                    continue
            new_data = (pos_a, pos_b, score_a, score_b, not a_active)
            if new_data in counts:
                counts[new_data] += num * n
            else:
                counts[new_data] = num * n
                q.put(new_data)
        # print(counts)

    print()
    print(wins_a)
    print(wins_b)
    print()

    return max(wins_a, wins_b)


def solve(data: InputType) -> list[str]:
    """Solve the puzzle for the given input."""
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(data)

    ret = [str(solution1)]
    if solution2 is not None:
        ret.append(str(solution2))

    return ret


if __name__ == "__main__":
    data = parse(get_data(year=2021, day=21))
    print("\n".join(solve(data)))
