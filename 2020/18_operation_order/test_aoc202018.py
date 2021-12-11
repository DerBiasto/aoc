"""Tests for AoC 18, 2020: Operation Order"""

# Standard library imports
import pathlib

# Third party imports
import aoc202018
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202018.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202018.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202018.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202018.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202018.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202018.parse(puzzle_input)


def test_parse_example1(example1: aoc202018.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1[0] == "1 + ( 2 * 3 ) + ( 4 * ( 5 + 6 ) )".split()


def test_part1_example1(example1: aoc202018.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202018.part1(example1) == sum([51, 26,  437, 12240, 13632])


def test_part1_puzzle_input(puzzle_input: aoc202018.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202018.part1(puzzle_input) == 1890866893020


def test_part2_example1(example1: aoc202018.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202018.part2(example1) == sum([51, 46, 1445, 669060, 23340])


@pytest.mark.skip
def test_part2_example2(example2: aoc202018.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202018.part2(example2) == 89026560


def test_part2_puzzle_input(puzzle_input: aoc202018.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202018.part2(puzzle_input) == 34646237037193
