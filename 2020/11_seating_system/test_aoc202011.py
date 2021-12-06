"""Tests for AoC 11, 2020: Seating System"""

# Standard library imports
import pathlib

# Third party imports
import aoc202011
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202011.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202011.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202011.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202011.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202011.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202011.parse(puzzle_input)


def test_parse_example1(example1: aoc202011.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1._grid == [
        list("L.LL.LL.LL"),
        list("LLLLLLL.LL"),
        list("L.L.L..L.."),
        list("LLLL.LL.LL"),
        list("L.LL.LL.LL"),
        list("L.LLLLL.LL"),
        list("..L.L....."),
        list("LLLLLLLLLL"),
        list("L.LLLLLL.L"),
        list("L.LLLLL.LL"),
    ]


def test_part1_example1(example1: aoc202011.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202011.part1(example1) == 37


def test_part1_puzzle_input(puzzle_input: aoc202011.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202011.part1(puzzle_input) == 2361


def test_part2_example1(example1: aoc202011.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202011.part2(example1) == 26


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202011.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202011.part2(example2) == ...


def test_part2_puzzle_input(puzzle_input: aoc202011.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202011.part2(puzzle_input) == 2315
