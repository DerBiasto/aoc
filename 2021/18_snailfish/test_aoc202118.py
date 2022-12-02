"""Tests for AoC 18, 2021: Snailfish"""

# Standard library imports
import pathlib

# Third party imports
import aoc202118
import pytest

SN = aoc202118.SnailfishNumber

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202118.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202118.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202118.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202118.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202118.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202118.parse(puzzle_input)


def test_parse_example1(example1: aoc202118.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1[0] == SN(SN(SN(0, SN(5, 8)), SN(SN(1, 7), SN(9, 6))), SN(SN(4, SN(1, 2)), SN(SN(1, 4), 2)))


def test_part1_example1(example1: aoc202118.InputType) -> None:
    """Test part 1 on example input"""
    assert SN(1, 2) + SN(3, 4) == SN(SN(1, 2), SN(3, 4))
    assert SN(1, 1) + SN(2, 2) + SN(3, 3) == SN(SN(SN(1, 1), SN(2, 2)), SN(3, 3))
    assert SN(1, 1) + SN(2, 2) + SN(3, 3) + SN(4, 4) == SN(SN(SN(SN(1, 1), SN(2, 2)), SN(3, 3)), SN(4, 4))
    assert str(SN(1, 1) + SN(2, 2) + SN(3, 3) + SN(4, 4) + SN(5, 5)) == str(SN(SN(SN(SN(3, 0), SN(5, 3)), SN(4, 4)), SN(5, 5)))
    # assert aoc202118.part1(example1) == 4140


@pytest.mark.skip(reason="Not implemented")
def test_part1_puzzle_input(puzzle_input: aoc202118.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202118.part1(puzzle_input) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: aoc202118.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202118.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202118.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202118.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202118.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202118.part2(puzzle_input) == ...
