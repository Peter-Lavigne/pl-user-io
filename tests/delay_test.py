from datetime import timedelta

from pl_user_io.assert_yes import assert_yes
from pl_user_io.delay import delay
from pl_user_io.display import display
from pl_user_io.task import task
from tests.conftest import with_pytestmarks
from tests.constants import PYTEST_MANUAL_MARKERS


@with_pytestmarks(*PYTEST_MANUAL_MARKERS)
def test_pauses_execution() -> None:
    task("After pressing enter, start counting from 0 until `Done.` is printed.")
    delay(timedelta(seconds=5))
    display("Done.")
    assert_yes("Did it take 5 seconds to print `Done.`?")
