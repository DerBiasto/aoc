"""Tests for AoC 3, 2021: Binary Diagnostic"""

# Standard library imports
import pathlib

# Third party imports
import aoc202103
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202103.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202103.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202103.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202103.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202103.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202103.parse(puzzle_input)


def test_parse_example1(example1) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


@pytest.mark.skip(reason="Not implemented")
def test_part1_puzzle_input(puzzle_input):
    """Test part 1 on full input."""
    assert aoc202103.part1(puzzle_input) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1) -> None:
    """Test part 1 on example input"""
    assert aoc202103.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202103.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc202103.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input):
    """Test part 2 on example input."""
    assert aoc202103.part2(puzzle_input) == ...
