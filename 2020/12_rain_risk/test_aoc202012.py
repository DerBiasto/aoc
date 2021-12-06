"""Tests for AoC 12, 2020: Rain Risk"""

# Standard library imports
import pathlib

# Third party imports
import aoc202012
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202012.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202012.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202012.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202012.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202012.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202012.parse(puzzle_input)


def test_parse_example1(example1: aoc202012.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        ("F", 10),
        ("N", 3),
        ("F", 7),
        ("R", 90),
        ("F", 11),
    ]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1: aoc202012.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202012.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_puzzle_input(puzzle_input: aoc202012.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202012.part1(puzzle_input) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: aoc202012.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202012.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202012.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202012.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202012.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202012.part2(puzzle_input) == ...
