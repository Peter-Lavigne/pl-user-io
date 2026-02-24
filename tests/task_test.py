from pl_mocks_and_fakes import mock_for

from pl_user_io.task import task
from pl_user_io.testing.user_io_fake import assert_displayed
from pl_user_io.wait_for_enter import wait_for_enter


def test_displays_instruction() -> None:
    task("This is a test task.")

    assert_displayed("This is a test task.")


def test_waits_for_user_to_complete_task() -> None:
    task("This is a test task.")

    mock_for(wait_for_enter).assert_called_once()
