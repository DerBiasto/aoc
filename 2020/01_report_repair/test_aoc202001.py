"""Tests for AoC 1, 2020: Report Repair"""

# Standard library imports
import pathlib

# Third party imports
import aoc202001
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202001.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202001.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202001.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202001.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202001.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202001.parse(puzzle_input)


def test_parse_example1(example1: aoc202001.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [1721, 979, 366, 299, 675, 1456]


def test_part1_example1(example1: aoc202001.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202001.part1(example1) == 514579


def test_part1_puzzle_input(puzzle_input: aoc202001.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202001.part1(puzzle_input) == 926464


def test_part2_example1(example1: aoc202001.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202001.part2(example1) == 241861950


def test_part2_puzzle_input(puzzle_input: aoc202001.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202001.part2(puzzle_input) == 65656536
