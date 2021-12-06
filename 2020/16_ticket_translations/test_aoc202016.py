"""Tests for AoC 16, 2020: Ticket Translations"""

# Standard library imports
import pathlib

# Third party imports
import aoc202016
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202016.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202016.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202016.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202016.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202016.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202016.parse(puzzle_input)


def test_parse_example1(example1: aoc202016.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == (
        {"class": (1, 3, 5, 7), "row": (6, 11, 33, 44), "seat": (13, 40, 45, 50)},
        (7, 1, 14),
        [
            (7, 3, 47),
            (40, 4, 50),
            (55, 2, 20),
            (38, 6, 12),
        ]
    )


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1: aoc202016.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202016.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_puzzle_input(puzzle_input: aoc202016.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202016.part1(puzzle_input) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: aoc202016.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202016.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202016.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202016.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202016.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202016.part2(puzzle_input) == ...
