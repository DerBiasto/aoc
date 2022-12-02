"""Tests for AoC 21, 2021: Dirac Dice"""

# Standard library imports
import pathlib

# Third party imports
import aoc202121
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202121.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202121.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202121.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202121.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202121.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202121.parse(puzzle_input)


def test_parse_example1(example1: aoc202121.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == (4, 8)


def test_part1_example1(example1: aoc202121.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202121.part1(example1) == 745 * 993 == 739785


def test_part1_puzzle_input(puzzle_input: aoc202121.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202121.part1(puzzle_input) == 605070


def test_part2_example1(example1: aoc202121.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202121.part2(example1) == 444356092776315

444356092776315
430229563871565

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202121.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202121.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202121.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202121.part2(puzzle_input) == ...
