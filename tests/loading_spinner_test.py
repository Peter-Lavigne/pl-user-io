from datetime import timedelta

import pytest

from pl_user_io.assert_yes import assert_yes
from pl_user_io.delay import delay
from pl_user_io.loading_spinner import loading_spinner
from tests.conftest import with_pytestmarks
from tests.constants import PYTEST_DEPENDENT_MARKER, PYTEST_MANUAL_MARKERS


@with_pytestmarks(*PYTEST_MANUAL_MARKERS)
def test_loading_spinner_passes() -> None:
    with loading_spinner("Testing status update"):
        delay(timedelta(seconds=3))

    assert_yes(
        "Did a 3-second loading spinner appear, then get replaced with a green check mark?"
    )
    assert_yes("Did it look good?")


@with_pytestmarks(*PYTEST_MANUAL_MARKERS)
def test_loading_spinner_failure() -> None:
    try:
        with (
            loading_spinner("Testing status update failure"),
        ):
            delay(timedelta(seconds=3))
            msg = "Simulated failure"
            raise RuntimeError(msg)
    except RuntimeError:
        pass

    assert_yes("Did a 3-second loading spinner appear, then get replaced with a red X?")
    assert_yes("Did it look good?")


@with_pytestmarks(PYTEST_DEPENDENT_MARKER)
def test_loading_spinner_failure_propagates_exception() -> None:
    failure_message = "Failure message"
    with (
        pytest.raises(RuntimeError, match=failure_message),
        loading_spinner("Testing status update failure"),
    ):
        raise RuntimeError(failure_message)
