from unittest.mock import Mock

from pl_user_io.str_input import StrInputResponse, str_input
from tests.constants import PYTEST_INTEGRATION_MARKER
from tests.user_io_fake import InputMappingCallback, user_io_fake

pytestmark = PYTEST_INTEGRATION_MARKER

StrInputMock = Mock


def stub_str_input_callback(callback: InputMappingCallback) -> None:
    user_io_fake().input_mapping_callbacks.insert(0, callback)


def stub_str_input(response: StrInputResponse, prior_output: str) -> None:
    def _callback(output: str) -> StrInputResponse | None:
        if output.endswith(prior_output):
            return response
        return None

    user_io_fake().input_mapping_callbacks.insert(0, _callback)


def input_count(mock: StrInputMock) -> int:
    return mock.call_count


def test_asks_for_user_input() -> None:
    result = str_input("Enter 'test':")

    assert result == "test"


def test_there_is_a_space_between_prompt_and_input() -> None:
    result = str_input(
        "If there is a space between this prompt and your input, enter 'yes'. Otherwise, enter 'no'."
    )

    assert result == "yes"
