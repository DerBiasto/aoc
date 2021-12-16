"""Tests for AoC 16, 2021: Packet Decoder"""

# Standard library imports
import pathlib

# Third party imports
import aoc202116
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202116.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202116.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202116.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202116.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202116.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202116.parse(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1: aoc202116.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == ...


def test_part1_example1(example1: aoc202116.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202116.part1(example1) == [16, 12, 23, 31]


def test_part1_puzzle_input(puzzle_input: aoc202116.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202116.part1(puzzle_input) == [886]


def test_part2_example1(example1: aoc202116.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202116.part2(example1) == [15, 46, 46, 54]


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202116.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202116.part2(example2) == ...


def test_part2_puzzle_input(puzzle_input: aoc202116.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202116.part2(puzzle_input) == [184487454837]
