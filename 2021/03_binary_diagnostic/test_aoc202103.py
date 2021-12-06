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


def test_parse_example1(example1: aoc202103.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == (5, [
        0b00100,
        0b11110,
        0b10110,
        0b10111,
        0b10101,
        0b01111,
        0b00111,
        0b11100,
        0b10000,
        0b11001,
        0b00010,
        0b01010,
    ])


def test_parse_puzzle_input(puzzle_input: aoc202103.InputType) -> None:
    assert puzzle_input[0] == 12


def test_part1_puzzle_input(puzzle_input: aoc202103.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202103.part1(puzzle_input) == 2954600


def test_part1_example1(example1: aoc202103.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202103.part1(example1) == 198


def test_part1_example2(example2: aoc202103.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202103.part1(example2) == 386463119445733053722557199393548794069517420395751036911156


def test_part2_example1(example1: aoc202103.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202103.part2(example1) == 230


def test_part2_example2(example2: aoc202103.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202103.part2(example2) == 356913958942791247617705918285570893096041618195840162127310


def test_part2_puzzle_input(puzzle_input: aoc202103.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202103.part2(puzzle_input) == 1662846
