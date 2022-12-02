"""Tests for AoC 19, 2021: BEacon Scanner"""

# Standard library imports
import pathlib

# Third party imports
import aoc202119
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example0() -> aoc202119.InputType:
    return aoc202119.parse("""--- scanner 0 ---
0,2
4,1
3,3

--- scanner 1 ---
-1,-1
-5,0
-2,1""")


@pytest.fixture
def example1() -> aoc202119.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202119.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202119.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202119.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202119.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202119.parse(puzzle_input)


def test_parse(example0: aoc202119.InputType) -> None:
    """Test that input is parsed properly."""
    assert example0 == {
        0: {
            (0, 2),
            (4, 1),
            (3, 3),
        },
        1: {
            (-1, -1),
            (-5, 0),
            (-2, 1),
        }
    }


def test_part1_example1(example1: aoc202119.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202119.part1(example1) == 79


@pytest.mark.skip(reason="Not implemented")
def test_part1_puzzle_input(puzzle_input: aoc202119.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202119.part1(puzzle_input) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: aoc202119.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202119.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202119.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202119.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202119.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202119.part2(puzzle_input) == ...
