"""Tests for AoC 24, 2020: Lobby Layout"""

# Standard library imports
import pathlib

# Third party imports
import aoc202024
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202024.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202024.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202024.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202024.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202024.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202024.parse(puzzle_input)


def test_parse_example1(example1: aoc202024.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        "sesenwnenenewseeswwswswwnenewsewsw",
        "neeenesenwnwwswnenewnwwsewnenwseswesw",
        "seswneswswsenwwnwse",
        "nwnwneseeswswnenewneswwnewseswneseene",
        "swweswneswnenwsewnwneneseenw",
        "eesenwseswswnenwswnwnwsewwnwsene",
        "sewnenenenesenwsewnenwwwse",
        "wenwwweseeeweswwwnwwe",
        "wsweesenenewnwwnwsenewsenwwsesesenwne",
        "neeswseenwwswnwswswnw",
        "nenwswwsewswnenenewsenwsenwnesesenew",
        "enewnwewneswsewnwswenweswnenwsenwsw",
        "sweneswneswneneenwnewenewwneswswnese",
        "swwesenesewenwneswnwwneseswwne",
        "enesenwswwswneneswsenwnewswseenwsese",
        "wnwnesenesenenwwnenwsewesewsesesew",
        "nenewswnwewswnenesenwnesewesw",
        "eneswnwswnwsenenwnwnwwseeswneewsenese",
        "neswnwewnwnwseenwseesewsenwsweewe",
        "wseweeenwnesenwwwswnew",
    ]


def test_part1_example1(example1: aoc202024.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202024.part1(example1) == 10


def test_part1_puzzle_input(puzzle_input: aoc202024.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202024.part1(puzzle_input) == 289


def test_part2_example1(example1: aoc202024.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202024.part2(example1) == 2208


def test_neighbours() -> None:
    assert aoc202024.get_neighbours(0, 0) == [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]
    assert aoc202024.get_neighbours(1, 0) == [(2, 0), (0, 0), (1, 1), (1, -1), (2, 1), (0, -1)]


def test_update() -> None:
    assert aoc202024.update_tiles({(0, 0), (1, 0)}) == {(0, 0), (1, 0), (1, 1), (0, -1)}


@pytest.mark.skip(reason="Not implemented")
def test_part2_puzzle_input(puzzle_input: aoc202024.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202024.part2(puzzle_input) == ...
