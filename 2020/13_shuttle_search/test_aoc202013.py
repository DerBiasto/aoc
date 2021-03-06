"""Tests for AoC 13, 2020: Shuttle Search"""

# Standard library imports
import pathlib

# Third party imports
import aoc202013
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202013.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202013.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202013.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202013.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202013.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202013.parse(puzzle_input)


def test_parse_example1(example1: aoc202013.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == (939, [7, 13, 0, 0, 59, 0, 31, 19])


def test_part1_example1(example1: aoc202013.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202013.part1(example1) == 295


def test_part1_puzzle_input(puzzle_input: aoc202013.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202013.part1(puzzle_input) == 4782


def test_part2_example1(example1: aoc202013.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202013.part2(example1) == 1068781


def test_part2_example2(example2: aoc202013.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202013.part2(example2) == 3417


def test_part2_puzzle_input(puzzle_input: aoc202013.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202013.part2(puzzle_input) == 1118684865113056
