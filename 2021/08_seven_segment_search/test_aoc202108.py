"""Tests for AoC 8, 2021: Seven Segment Search"""

# Standard library imports
import pathlib

# Third party imports
import aoc202108
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202108.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202108.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202108.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202108.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202108.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202108.parse(puzzle_input)


def test_parse_example1(example1: aoc202108.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1[0] == (
        ["be", "bde", "bceg", "abcdf", "bcdef", "cdefg", "abdefg", "acdefg", "bcdefg", "abcdefg"],
        ["abcdefg", "bcdef", "bcdefg", "bceg"]
    )


def test_part1_example1(example1: aoc202108.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202108.part1(example1) == 26


def test_part1_puzzle_input(puzzle_input: aoc202108.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202108.part1(puzzle_input) == 278


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: aoc202108.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202108.part2(example1) == 61229


def test_part2_example2(example2: aoc202108.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202108.part2(example2) == 5353


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202108.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202108.part2(puzzle_input) == ...
