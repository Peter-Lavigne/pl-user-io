from pl_mocks_and_fakes import mock_for

from pl_user_io.str_input import str_input
from pl_user_io.testing.stubs import input_count, stub_str_input
from pl_user_io.yes_no import yes_no


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
