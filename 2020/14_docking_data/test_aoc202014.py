"""Tests for AoC 14, 2020: Docking Data"""

# Standard library imports
import pathlib

# Third party imports
import aoc202014
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202014.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202014.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202014.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202014.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202014.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202014.parse(puzzle_input)


def test_parse_example1(example1: aoc202014.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [(-1, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"), (8, 11), (7, 101), (8, 0)]


def test_part1_example1(example1: aoc202014.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202014.part1(example1) == 165


def test_part1_puzzle_input(puzzle_input: aoc202014.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202014.part1(puzzle_input) == 11501064782628


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: aoc202014.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202014.part2(example1) == ...


def test_part2_example2(example2: aoc202014.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202014.part2(example2) == 208


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202014.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202014.part2(puzzle_input) == ...
