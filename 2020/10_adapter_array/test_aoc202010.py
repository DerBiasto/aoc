"""Tests for AoC 10, 2020: Adapter Array"""

# Standard library imports
import pathlib

# Third party imports
import aoc202010
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202010.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202010.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202010.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202010.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202010.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202010.parse(puzzle_input)


def test_parse_example1(example1: aoc202010.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        16,
        10,
        15,
        5,
        1,
        11,
        7,
        19,
        6,
        12,
        4,
    ]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1: aoc202010.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202010.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_puzzle_input(puzzle_input: aoc202010.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202010.part1(puzzle_input) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: aoc202010.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202010.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202010.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202010.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202010.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202010.part2(puzzle_input) == ...
