import pytest

from pl_user_io.assert_yes import assert_yes
from pl_user_io.testing.stubs import stub_yes_no

ARBITRARY_QUESTION = "Is this a test?"


def test_does_nothing_if_yes() -> None:
    stub_yes_no(ARBITRARY_QUESTION, True)

    assert_yes(ARBITRARY_QUESTION)


def test_raises_assertion_error_if_no() -> None:
    stub_yes_no(ARBITRARY_QUESTION, False)

    with pytest.raises(AssertionError):
        assert_yes(ARBITRARY_QUESTION)
