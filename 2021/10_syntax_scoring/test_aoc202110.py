"""Tests for AoC 10, 2021: Syntax Scoring"""

# Standard library imports
import pathlib

# Third party imports
import aoc202110
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> aoc202110.InputType:
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202110.parse(puzzle_input)


@pytest.fixture
def example2() -> aoc202110.InputType:
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202110.parse(puzzle_input)


@pytest.fixture
def example3() -> aoc202110.InputType:
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc202110.parse(puzzle_input)


@pytest.fixture
def puzzle_input() -> aoc202110.InputType:
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc202110.parse(puzzle_input)


def test_parse_example1(example1: aoc202110.InputType) -> None:
    """Test that input is parsed properly."""
    assert example1 == [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]


def test_part1_example1(example1: aoc202110.InputType) -> None:
    """Test part 1 on example input"""
    assert aoc202110.part1(example1) == 26397


def test_part1_example2(example2: aoc202110.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202110.part1(example2) == 32852823


def test_part1_puzzle_input(puzzle_input: aoc202110.InputType) -> None:
    """Test part 1 on full input."""
    assert aoc202110.part1(puzzle_input) == 311895


def test_part2_example1(example1: aoc202110.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202110.part2(example1) == 288957


def test_part2_example2(example2: aoc202110.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202110.part2(example2) == 105721020868542718163333508098695965856824383141538359


def test_part2_example3(example3: aoc202110.InputType) -> None:
    """Test part 2 on example input"""
    assert aoc202110.part2(example3) == 4147221136278686118851251078439942241593032865422495540589075652007224217627158672406548941332753773231145137591607755327259751330408129749234363801432056312168742919300272994666758197001661058825916005929107429822715605939942443473451119156732403958992327362236310858256528168096490885509843074970456349764872605113646021900154182133457634302249036648560726381663678169920580181158091185711536415744289810493158025390014526746339533063857301193312008845372928578055750021478792579394195467723166421532710570596861139275905662620238


def test_part2_puzzle_input(puzzle_input: aoc202110.InputType) -> None:
    """Test part 2 on example input."""
    assert aoc202110.part2(puzzle_input) == 2904180541
