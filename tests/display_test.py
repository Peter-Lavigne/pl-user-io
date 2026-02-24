from pl_user_io.assert_yes import assert_yes
from pl_user_io.display import display
from tests.conftest import with_pytestmarks
from tests.constants import PYTEST_MANUAL_MARKERS


@with_pytestmarks(*PYTEST_MANUAL_MARKERS)
def test_output() -> None:
    display("1")

    assert_yes("Did the output '1' appear on the screen?")
