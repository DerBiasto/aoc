"""Tests for AoC 13, 2021: Transparent Origami"""

# Standard library imports
import pathlib

# Third party imports
import aoc202113
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202113.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202113.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202113.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202113.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202113.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202113.parse(puzzle_input)


def test_parse_example1(example1: aoc202113.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == (
        {
            (6, 10),
            (0, 14),
            (9, 10),
            (0, 3),
            (10, 4),
            (4, 11),
            (6, 0),
            (6, 12),
            (4, 1),
            (0, 13),
            (10, 12),
            (3, 4),
            (3, 0),
            (8, 4),
            (1, 10),
            (2, 14),
            (8, 10),
            (9, 0),
        },
        [
            ("y", 7),
            ("x", 5),
        ]
    )


def test_part1_example1(example1: aoc202113.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202113.part1(example1) == 17


def test_part1_puzzle_input(puzzle_input: aoc202113.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202113.part1(puzzle_input) == 942


def test_part2_example1(example1: aoc202113.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202113.part2(example1).split("\n") == [
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#####",
    ]


def test_part2_example2(example2: aoc202113.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202113.part2(example2).split("\n") == [
        "#     # ####### #     # ####### ######      #####  ####### #     # #     #    #        #####  ### #     # #######    #     # ####### #     #    #     # ###### ",
        "##    # #       #     # #       #     #    #     # #     # ##    # ##    #   # #      #     #  #  #     # #           #   #  #     # #     #    #     # #     #",
        "# #   # #       #     # #       #     #    #       #     # # #   # # #   #  #   #     #        #  #     # #            # #   #     # #     #    #     # #     #",
        "#  #  # #####   #     # #####   ######     #  #### #     # #  #  # #  #  # #     #    #  ####  #  #     # #####         #    #     # #     #    #     # ###### ",
        "#   # # #        #   #  #       #   #      #     # #     # #   # # #   # # #######    #     #  #   #   #  #             #    #     # #     #    #     # #      ",
        "#    ## #         # #   #       #    #     #     # #     # #    ## #    ## #     #    #     #  #    # #   #             #    #     # #     #    #     # #      ",
        "#     # #######    #    ####### #     #     #####  ####### #     # #     # #     #     #####  ###    #    #######       #    #######  #####      #####  #      ",
    ]


def test_part2_puzzle_input(puzzle_input: aoc202113.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202113.part2(puzzle_input).split("\n") == [
        "  ## ####  ##  #  #  ##  ###  ###  ### ",
        "   #    # #  # #  # #  # #  # #  # #  #",
        "   #   #  #    #  # #  # #  # #  # ### ",
        "   #  #   # ## #  # #### ###  ###  #  #",
        "#  # #    #  # #  # #  # #    # #  #  #",
        " ##  ####  ###  ##  #  # #    #  # ### ",
    ]
