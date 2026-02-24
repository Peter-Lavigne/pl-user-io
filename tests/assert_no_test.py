import pytest

from pl_user_io.assert_no import assert_no
from pl_user_io.testing.stubs import stub_yes_no

ARBITRARY_QUESTION = "Is this a test?"


def test_does_nothing_if_no() -> None:
    stub_yes_no(ARBITRARY_QUESTION, False)

    assert_no(ARBITRARY_QUESTION)


def test_raises_assertion_error_if_yes() -> None:
    stub_yes_no(ARBITRARY_QUESTION, True)

    with pytest.raises(AssertionError):
        assert_no(ARBITRARY_QUESTION)
