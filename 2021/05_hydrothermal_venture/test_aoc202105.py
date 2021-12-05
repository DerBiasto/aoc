"""Tests for AoC 5, 2021: Hydrothermal Venture"""

# Standard library imports
import pathlib

# Third party imports
import aoc202105
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202105.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202105.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202105.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202105.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202105.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202105.parse(puzzle_input)


def test_parse_example1(example1) -> None:
    """Test that input is parsed properly."""
    for line in example1:
        assert isinstance(line, aoc202105.Line)
    temp = [
        ((line.start.x, line.start.y), (line.end.x, line.end.y))
        for line in example1
    ]
    assert temp == [
        ((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((9, 4), (3, 4)),
        ((2, 2), (2, 1)),
        ((7, 0), (7, 4)),
        ((6, 4), (2, 0)),
        ((0, 9), (2, 9)),
        ((3, 4), (1, 4)),
        ((0, 0), (8, 8)),
        ((5, 5), (8, 2)),
    ]


def test_part1_puzzle_input(puzzle_input):
    """Test part 1 on full input."""
    assert aoc202105.part1(puzzle_input) == 5294


def test_part1_example1(example1) -> None:
    """Test part 1 on example input"""
    assert aoc202105.part1(example1) == 5


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202105.part2(example1) == 12


def test_part2_puzzle_input(puzzle_input):
    """Test part 2 on example input."""
    assert aoc202105.part2(puzzle_input) == 21698
