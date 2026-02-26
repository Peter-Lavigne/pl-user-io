from pl_mocks_and_fakes import mock_for

from pl_user_io.int_input import int_input
from pl_user_io.str_input import str_input
from pl_user_io.testing import (
    input_count,
    stub_str_input,
)


def test_returns_integer() -> None:
    stub_str_input("5", "")

    result = int_input("Provide the value '5'.")

    assert result == 5


def test_reprompts_for_invalid_input() -> None:
    stub_str_input("", "")
    stub_str_input("invalid", "")
    stub_str_input("5.5", "")
    stub_str_input("5", "")

    result = int_input("Try invalid inputs, then respond with '5'.")

    assert result == 5
    assert input_count(mock_for(str_input)) == 4
