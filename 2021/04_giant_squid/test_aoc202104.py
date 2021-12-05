"""Tests for AoC 4, 2021: Giant Squid"""

# Standard library imports
import pathlib

# Third party imports
import aoc202104
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202104.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202104.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202104.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202104.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202104.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202104.parse(puzzle_input)


def test_parse_example1(example1) -> None:
    """Test that input is parsed properly."""
    assert example1[0] == [
        7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1,
    ]
    for b in example1[1]:
        assert isinstance(b, aoc202104.Board)


def test_part1_puzzle_input(puzzle_input):
    """Test part 1 on full input."""
    assert aoc202104.part1(puzzle_input) == 55770


def test_part1_example1(example1) -> None:
    """Test part 1 on example input"""
    assert aoc202104.part1(example1) == 4512


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202104.part2(example1) == 1924


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input):
    """Test part 2 on example input."""
    assert aoc202104.part2(puzzle_input) == ...
