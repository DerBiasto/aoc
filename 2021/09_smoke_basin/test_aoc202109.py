"""Tests for AoC 9, 2021: Smoke Basin"""

# Standard library imports
import pathlib

# Third party imports
import aoc202109
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202109.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202109.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202109.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202109.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202109.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202109.parse(puzzle_input)


def test_parse_example1(example1: aoc202109.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]


def test_part1_example1(example1: aoc202109.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202109.part1(example1) == 15


def test_part1_puzzle_input(puzzle_input: aoc202109.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202109.part1(puzzle_input) == 462


def test_part2_example1(example1: aoc202109.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202109.part2(example1) == 1134


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202109.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202109.part2(example2) == ...


def test_part2_puzzle_input(puzzle_input: aoc202109.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202109.part2(puzzle_input) == 1397760
