from pl_user_io.assert_yes import assert_yes
from pl_user_io.display import display
from pl_user_io.wait_for_enter import wait_for_enter
from tests.constants import PYTEST_INTEGRATION_MARKER

pytestmark = PYTEST_INTEGRATION_MARKER


def test_success() -> None:
    wait_for_enter()

    assert_yes("Did the prompt wait for you to press 'enter'?")


def test_checkmark() -> None:
    wait_for_enter()

    assert_yes("Did the prompt display a checkmark after you pressed 'enter'?")


def test_handles_non_enter() -> None:
    display("Press a few keys other than 'enter' before pressing 'enter'.")

    wait_for_enter()

    assert_yes("Did the prompt wait for you to press enter?")
