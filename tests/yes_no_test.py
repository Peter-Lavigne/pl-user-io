from pl_mocks_and_fakes import mock_for

from pl_user_io.str_input import str_input
from pl_user_io.yes_no import yes_no
from tests.str_input_test import input_count, stub_str_input
from tests.user_io_fake import (
    assert_displayed,
    assert_displayed_exactly_once,
    assert_not_displayed,
)


def assert_asked_yes_no(question: str) -> None:
    """Assert that the yes/no question was asked to the user."""
    assert_displayed(f"{question} (y/n)")


def assert_asked_yes_no_exactly_once(question: str) -> None:
    assert_displayed_exactly_once(f"{question} (y/n)")


def assert_not_asked_yes_no(question: str) -> None:
    assert_not_displayed(f"{question} (y/n)")


def stub_yes_no(question: str, answer: bool) -> None:
    stub_str_input("y" if answer else "n", f"{question} (y/n)")


def test_returns_true_for_yes() -> None:
    stub_str_input("y", "")

    result = yes_no("Respond 'y' (yes) to this prompt.")

    assert result


def test_returns_false_for_no() -> None:
    stub_str_input("n", "")

    result = yes_no("Respond 'n' (no) to this prompt.")

    assert not result


def test_retries_invalid_input() -> None:
    stub_str_input("", "")
    stub_str_input("invalid", "")
    stub_str_input("yes", "")
    stub_str_input("y", "")

    result = yes_no("Try invalid inputs, then respond with 'y'.")

    assert result
    assert input_count(mock_for(str_input)) == 4
