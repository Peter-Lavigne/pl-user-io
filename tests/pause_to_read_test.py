import random

from pl_user_io.display import display
from pl_user_io.pause_to_read import pause_to_read
from pl_user_io.task import task
from pl_user_io.yes_no import yes_no
from tests.constants import PYTEST_INTEGRATION_MARKER

pytestmark = PYTEST_INTEGRATION_MARKER


def _assert_readable() -> None:
    # overrwite the previous line
    display("\033[F\033[K", end="")
    display("Stop reading.")
    assert yes_no("Was the stop timer appropriate?")


def test_pauses_long_enough__simulated() -> None:
    task("Mentally prepare to start the test.")

    instructions = [
        "Prepare to do something.",
        "Understand me.",
        "Be sure to read the whole thing since it's important.",
        "Continue reading until you reach the end.",
    ]
    # This makes the test non-deterministic, but I want to avoid memorizing the prompts
    # I suppose that I, myself, am non-deterministic.
    random.shuffle(instructions)

    for i in range(len(instructions)):
        text = " ".join(instructions[: i + 1])
        display(text)
        pause_to_read(text)
        _assert_readable()


def test_pauses_long_enough__real_examples() -> None:
    task("Mentally prepare to start the test.")

    text = "All done. Leave for work."
    display(text)
    pause_to_read(text)
    _assert_readable()
