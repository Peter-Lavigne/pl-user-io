from pl_user_io.assert_no import assert_no
from pl_user_io.assert_yes import assert_yes
from pl_user_io.open_url import open_url
from pl_user_io.task import task
from tests.constants import PYTEST_MANUAL_MARKERS

pytestmark = PYTEST_MANUAL_MARKERS


def test_opens_url() -> None:
    open_url("https://www.example.com/")

    assert_yes("Was example.com opened in a browser?")


def test_displays_no_extra_output_when_browser_closed() -> None:
    task("Quit firefox.")

    open_url("https://www.example.com/")

    assert_no("Check the terminal output. Was unexpected output displayed?")
