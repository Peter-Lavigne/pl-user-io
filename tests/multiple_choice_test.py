from pl_mocks_and_fakes import mock_for

from pl_user_io.multiple_choice import multiple_choice
from pl_user_io.str_input import str_input
from pl_user_io.testing import input_count, stub_str_input
from pl_user_io.testing.assertions import (
    assert_multiple_choice_displayed,
)
from pl_user_io.testing.helpers import options_for_multiple_choice

type Question = str
type Answer = str


def test_displays_qustion_and_options() -> None:
    stub_str_input("2", "")

    multiple_choice("Choose 'B'", [("A", 100), ("B", 200), ("C", 300)])

    assert_multiple_choice_displayed("Choose 'B'")
    assert options_for_multiple_choice("Choose 'B'") == [
        "A",
        "B",
        "C",
    ]


def test_returns_chosen_value() -> None:
    stub_str_input("2", "")

    # Using hundreds-values to avoid accidentally testing the selection or indices.
    result = multiple_choice("Choose 'B'", [("A", 100), ("B", 200), ("C", 300)])

    assert result == 200


def test_reprompts_for_invalid_input() -> None:
    stub_str_input("", "")
    stub_str_input("invalid", "")
    stub_str_input("10", "")
    stub_str_input("2", "")

    result = multiple_choice(
        "Provide invalid inputs ('f', '5', etc.), then choose B:",
        [("A", 100), ("B", 200), ("C", 300)],
    )

    assert result == 200
    assert input_count(mock_for(str_input)) == 4


def test_only_allows_positive_number_inputs() -> None:
    stub_str_input("-1", "")
    stub_str_input("0", "")
    stub_str_input("2", "")

    result = multiple_choice(
        "Provide invalid inputs ('-1', '0', etc.), then choose B:",
        [("A", 100), ("B", 200), ("C", 300)],
    )

    assert result == 200
    assert input_count(mock_for(str_input)) == 3
