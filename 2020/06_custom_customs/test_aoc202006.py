"""Tests for AoC 6, 2020: Custom Customs"""

# Standard library imports
import pathlib

# Third party imports
import aoc202006
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202006.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202006.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202006.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202006.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202006.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202006.parse(puzzle_input)


def test_parse_example1(example1: aoc202006.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        [{"a", "b", "c"}],
        [{"a"}, {"b"}, {"c"}],
        [{"a", "b"}, {"a", "c"}],
        [{"a"}, {"a"}, {"a"}, {"a"}],
        [{"b"}],
    ]


def test_part1_example1(example1: aoc202006.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202006.part1(example1) == 11


def test_part1_puzzle_input(puzzle_input: aoc202006.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202006.part1(puzzle_input) == 6763


def test_part2_example1(example1: aoc202006.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202006.part2(example1) == 6


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202006.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202006.part2(example2) == ...


def test_part2_puzzle_input(puzzle_input: aoc202006.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202006.part2(puzzle_input) == 3512
