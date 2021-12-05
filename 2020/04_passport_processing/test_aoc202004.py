"""Tests for AoC 4, 2020: Passport Processing"""

# Standard library imports
import pathlib

# Third party imports
import aoc202004
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202004.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202004.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202004.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202004.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202004.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202004.parse(puzzle_input)


def test_parse_example1(example1: aoc202004.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        {"ecl": "gry", "pid": "860033327", "eyr": "2020", "hcl": "#fffffd", "byr": "1937", "iyr": "2017", "cid": "147",
         "hgt": "183cm"},
        {"iyr": "2013", "ecl": "amb", "cid": "350", "eyr": "2023", "pid": "028048884", "hcl": "#cfa07d", "byr": "1929"},
        {"hcl": "#ae17e1", "iyr": "2013", "eyr": "2024", "ecl": "brn", "pid": "760753108", "byr": "1931",
         "hgt": "179cm"},
        {"hcl": "#cfa07d", "eyr": "2025", "pid": "166559648", "iyr": "2011", "ecl": "brn", "hgt": "59in"},
    ]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1: aoc202004.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202004.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_puzzle_input(puzzle_input: aoc202004.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202004.part1(puzzle_input) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1: aoc202004.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202004.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: aoc202004.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202004.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202004.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202004.part2(puzzle_input) == ...
