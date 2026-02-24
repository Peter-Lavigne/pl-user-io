from pl_mocks_and_fakes import mock_for

from pl_user_io.open_url import open_url
from pl_user_io.pause_to_read import pause_to_read
from pl_user_io.task_with_url import task_with_url


def test_opens_provided_url() -> None:
    task_with_url("Opening 'example.com'...", "https://www.example.com/")

    mock_for(open_url).assert_called_once_with("https://www.example.com/")


def test_pauses_to_read_task_if_opening_url() -> None:
    task_with_url("Opening 'example.com'...", "https://www.example.com/")

    mock_for(pause_to_read).assert_called_once_with("Opening 'example.com'...")
