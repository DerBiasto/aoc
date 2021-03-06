"""Tests for AoC 6, 2021: Lanternfish"""

# Standard library imports
import math
import pathlib

# Third party imports
import aoc202106
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202106.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202106.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202106.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202106.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202106.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202106.parse(puzzle_input)


def test_parse_example1(example1: aoc202106.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [3, 4, 3, 1, 2]


def test_part1_example1(example1: aoc202106.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202106.part1(example1) == 5934


def test_part1_puzzle_input(puzzle_input: aoc202106.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202106.part1(puzzle_input) == 352872


def test_part2_example1(example1: aoc202106.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202106.part2(example1) == 26984457539


def test_part2_puzzle_input(puzzle_input: aoc202106.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202106.part2(puzzle_input) == 1604361182149


def test_part3_example1(example1: aoc202106.InputType) -> None:
    assert int(math.log10(aoc202106.part3(example1))) + 1 == 378346
