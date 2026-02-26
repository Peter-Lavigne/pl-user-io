import pytest
from pl_mocks_and_fakes import mock_for

from pl_user_io.open_url import open_url
from pl_user_io.testing.helpers import all_instances_of_question
from pl_user_io.testing.user_io_fake import (
    assert_displayed,
    assert_displayed_exactly_once,
    assert_not_displayed,
)
from pl_user_io.wait_for_enter import WAIT_FOR_ENTER_TEXT


def assert_asked_yes_no(question: str) -> None:
    """Assert that the yes/no question was asked to the user."""
    assert_displayed(f"{question} (y/n)")


def assert_asked_yes_no_exactly_once(question: str) -> None:
    assert_displayed_exactly_once(f"{question} (y/n)")


def assert_not_asked_yes_no(question: str) -> None:
    assert_not_displayed(f"{question} (y/n)")


def assert_task_performed(task_str: str, url_opened: str | None = None) -> None:
    assert_displayed(f"{task_str}\n{WAIT_FOR_ENTER_TEXT}")
    if url_opened is not None:
        urls_opened = [call[0][0] for call in mock_for(open_url).call_args_list]
        assert url_opened in urls_opened


def assert_task_not_performed(task_str: str, url_opened: str | None = None) -> None:
    with pytest.raises(AssertionError):
        assert_task_performed(task_str, url_opened=url_opened)


def assert_loading_spinner_displayed(event: str) -> None:
    assert_displayed(f"✓ {event}")


def assert_multiple_choice_displayed(question: str) -> None:
    assert len(all_instances_of_question(question)) > 0


def assert_multiple_choice_not_displayed(question: str) -> None:
    assert len(all_instances_of_question(question)) == 0
