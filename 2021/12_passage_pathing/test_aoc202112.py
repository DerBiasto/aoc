"""Tests for AoC 12, 2021: Passage Pathing"""

# Standard library imports
import pathlib

# Third party imports
import aoc202112
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202112.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202112.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202112.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202112.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202112.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202112.parse(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1: aoc202112.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == ...


def test_part1_example1(example1: aoc202112.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202112.part1(example1) == 10


def test_part1_example2(example2: aoc202112.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202112.part1(example2) == 226


@pytest.mark.skip(reason="Not implemented")
def test_part1_puzzle_input(puzzle_input: aoc202112.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202112.part1(puzzle_input) == ...


def test_part2_example1(example1: aoc202112.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202112.part2(example1) == 36


def test_part2_example2(example2: aoc202112.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202112.part2(example2) == 3509


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202112.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202112.part2(puzzle_input) == ...
