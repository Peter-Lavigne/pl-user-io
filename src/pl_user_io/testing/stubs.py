import re
from collections.abc import Callable
from unittest.mock import Mock

from pl_user_io.str_input import StrInputResponse
from pl_user_io.testing.helpers import Answer, Question, all_instances_of_question
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


def stub_int_input(question: str, answer: int) -> None:
    stub_str_input(str(answer), f"{question}")


type IntInputMappingCallback = Callable[[str], int | None]


def stub_int_input_callback(callback: IntInputMappingCallback) -> None:
    stub_str_input_callback(
        lambda output: str(callback(output)) if callback(output) is not None else None,
    )


def _extract_answer_number(multiple_choice_output: str, answer: Answer) -> int:
    regex = rf"(\d+)\. {re.escape(answer)}"
    match = re.search(regex, multiple_choice_output, re.DOTALL)
    if match is None:
        msg = f"Failed to find answer `{answer}` in output: ```\n {multiple_choice_output}\n```"
        raise Exception(msg)
    return int(match.group(1))


def stub_multiple_choice(question: Question, answer: Answer) -> None:
    def _callback(output: str) -> int | None:
        result = all_instances_of_question(question)
        if len(result) != 0 and output.endswith(result[-1]):
            return _extract_answer_number(result[-1], answer)
        return None

    stub_int_input_callback(_callback)
