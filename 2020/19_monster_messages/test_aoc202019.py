"""Tests for AoC 19, 2020: Monster Messages"""

# Standard library imports
import pathlib

# Third party imports
import aoc202019
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202019.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202019.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202019.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202019.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202019.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202019.parse(puzzle_input)


def test_parse_example1(example1: aoc202019.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == (
        {
            "0": ["4 1 5"],
            "1": ["2 3", "3 2"],
            "2": ["4 4", "5 5"],
            "3": ["4 5", "5 4"],
            "4": ["a"],
            "5": ["b"],
        },
        [
            "ababbb",
            "bababa",
            "abbbab",
            "aaabbb",
            "aaaabbb",
        ]
    )


def test_part1_example1(example1: aoc202019.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202019.part1(example1) == 2


def test_part1_more() -> None:
    assert aoc202019.part1(({"0": ["a 1"], "1": ["a", "b"]}, ["ab", "aa", "aab"])) == 2


def test_part1_puzzle_input(puzzle_input: aoc202019.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202019.part1(puzzle_input) == 115


def test_part2_example1(example1: aoc202019.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202019.part2(example1) == 2


def test_part2_example2(example2: aoc202019.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202019.part2(example2) == 12


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202019.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202019.part2(puzzle_input) == 237
