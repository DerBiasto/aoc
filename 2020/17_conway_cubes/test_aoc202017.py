"""Tests for AoC 17, 2020: Conway Cubes"""

# Standard library imports
import pathlib

# Third party imports
import aoc202017
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202017.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202017.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202017.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202017.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202017.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202017.parse(puzzle_input)


def test_parse_example1(example1: aoc202017.InputType) -> None:
    """Test that input is parsed properly."""
    assert list(list(list(list(map(lambda c: c.state, row.values())) for row in layer.values()) for layer in cube.values()) for cube in example1.values()) == [
        [
            [
                [False, True, False],
                [False, False, True],
                [True, True, True],
            ]
        ]
    ]


def test_part1_example1(example1: aoc202017.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202017.part1(example1) == 112


def test_part1_puzzle_input(puzzle_input: aoc202017.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202017.part1(puzzle_input) == 257


def test_part2_example1(example1: aoc202017.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202017.part2(example1) == 848


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202017.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202017.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202017.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202017.part2(puzzle_input) == ...
