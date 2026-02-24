import pytest
from pl_mocks_and_fakes import mock_for

from pl_user_io.open_url import open_url
from pl_user_io.task import task
from pl_user_io.wait_for_enter import WAIT_FOR_ENTER_TEXT, wait_for_enter
from tests.user_io_fake import assert_displayed


def assert_task_performed(task_str: str, url_opened: str | None = None) -> None:
    assert_displayed(f"{task_str}\n{WAIT_FOR_ENTER_TEXT}")
    if url_opened is not None:
        urls_opened = [call[0][0] for call in mock_for(open_url).call_args_list]
        assert url_opened in urls_opened


def assert_task_not_performed(task_str: str, url_opened: str | None = None) -> None:
    with pytest.raises(AssertionError):
        assert_task_performed(task_str, url_opened=url_opened)


def test_displays_instruction() -> None:
    task("This is a test task.")

    assert_displayed("This is a test task.")


def test_waits_for_user_to_complete_task() -> None:
    task("This is a test task.")

    mock_for(wait_for_enter).assert_called_once()
