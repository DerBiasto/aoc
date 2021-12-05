"""Tests for AoC 2, 2020: Password Philosophy"""

# Standard library imports
import pathlib

# Third party imports
import aoc202002
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202002.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202002.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202002.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202002.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202002.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202002.parse(puzzle_input)


def test_parse_example1(example1: aoc202002.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        (1, 3, "a", "abcde"),
        (1, 3, "b", "cdefg"),
        (2, 9, "c", "ccccccccc"),
    ]


def test_part1_example1(example1: aoc202002.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202002.part1(example1) == 2


def test_part1_puzzle_input(puzzle_input: aoc202002.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202002.part1(puzzle_input) == 636


def test_part2_example1(example1: aoc202002.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202002.part2(example1) == 1


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202002.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202002.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202002.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202002.part2(puzzle_input) == ...
