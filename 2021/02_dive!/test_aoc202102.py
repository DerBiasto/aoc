"""Tests for AoC 2, 2021: Dive!"""

# Standard library imports
import pathlib

# Third party imports
import aoc202102
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202102.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202102.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202102.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202102.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202102.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202102.parse(puzzle_input)


def test_parse_example1(example1) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]


def test_part1_puzzle_input(puzzle_input):
    """Test part 1 on full input."""
    assert aoc202102.part1(puzzle_input) == 1561344


def test_part1_example1(example1) -> None:
    """Test part 1 on example input"""
    assert aoc202102.part1(example1) == 150


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202102.part2(example1) == 900


def test_part2_puzzle_input(puzzle_input):
    """Test part 2 on example input."""
    assert aoc202102.part2(puzzle_input) == 1848454425
