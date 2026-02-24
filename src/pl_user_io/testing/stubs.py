from unittest.mock import Mock

from pl_user_io.str_input import StrInputResponse
from pl_user_io.testing.user_io_fake import InputMappingCallback, user_io_fake

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


def stub_yes_no(question: str, answer: bool) -> None:
    stub_str_input("y" if answer else "n", f"{question} (y/n)")
