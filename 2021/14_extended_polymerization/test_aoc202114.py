"""Tests for AoC 14, 2021: Extended Polymerization"""

# Standard library imports
import pathlib

# Third party imports
import aoc202114
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202114.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202114.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202114.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202114.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202114.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202114.parse(puzzle_input)


def test_parse_example1(example1: aoc202114.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == (
        "NNCB",
        {
            "CH": "B",
            "HH": "N",
            "CB": "H",
            "NH": "C",
            "HB": "C",
            "HC": "B",
            "HN": "C",
            "NN": "C",
            "BH": "H",
            "NC": "B",
            "NB": "B",
            "BN": "B",
            "BB": "N",
            "BC": "B",
            "CC": "N",
            "CN": "C",
        }
    )


def test_part1_example1(example1: aoc202114.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202114.part1(example1) == 1588


def test_part1_puzzle_input(puzzle_input: aoc202114.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202114.part1(puzzle_input) == 2874


def test_part2_example1(example1: aoc202114.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202114.part2(example1) == 2188189693529


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202114.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202114.part2(example2) == ...


def test_part2_puzzle_input(puzzle_input: aoc202114.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202114.part2(puzzle_input) == 5208377027195
