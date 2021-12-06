"""Tests for AoC 8, 2020: Handheld Halting"""

# Standard library imports
import pathlib

# Third party imports
import aoc202008
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202008.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202008.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202008.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202008.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202008.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202008.parse(puzzle_input)


def test_parse_example1(example1: aoc202008.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        ("nop", 0),
        ("acc", 1),
        ("jmp", 4),
        ("acc", 3),
        ("jmp", -3),
        ("acc", -99),
        ("acc", 1),
        ("jmp", -4),
        ("acc", 6),
    ]


def test_part1_example1(example1: aoc202008.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202008.part1(example1) == 5


def test_part1_puzzle_input(puzzle_input: aoc202008.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202008.part1(puzzle_input) == 1766


def test_part2_example1(example1: aoc202008.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202008.part2(example1) == 8


def test_part2_puzzle_input(puzzle_input: aoc202008.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202008.part2(puzzle_input) == 1639
