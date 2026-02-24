import itertools
from collections.abc import Callable, Generator
from contextlib import contextmanager
from textwrap import dedent
from typing import Any, TypedDict

import pytest
from pl_mocks_and_fakes import Fake, fake_for, mock_for

from pl_user_io.display import display
from pl_user_io.loading_spinner import loading_spinner
from pl_user_io.str_input import StrInputParam, StrInputResponse, str_input
from pl_user_io.wait_for_enter import WAIT_FOR_ENTER_TEXT, wait_for_enter

InputMappingCallback = Callable[[str], str | None]


class PrintKwargs(TypedDict, total=False):
    end: str | None


class UserIOFake(Fake):
    def __init__(self) -> None:
        def _wait_for_enter_side_effect() -> None:
            self._add_to_output_str(f"{WAIT_FOR_ENTER_TEXT} ✓\n")

        def _str_input_side_effect(prompt: StrInputParam) -> StrInputResponse:
            self._add_to_output_str(prompt)

            for callback in reversed(self.input_mapping_callbacks):
                result = callback(self.output_str())
                if result is not None:
                    self.input_mapping_callbacks.remove(callback)
                    return result

            msg = f"No user input matching output: `{self.output_str()}`"
            raise Exception(msg)

        def _display_side_effect(
            *args: list[Any],
            end: str | None = "\n",
            flush: bool = False,  # noqa: ARG001
        ) -> None:
            if len(args) > 0:
                self._add_to_output_str(str(args[0]))
            self._add_to_output_str(str("\n" if end is None else end))

        @contextmanager
        def _loading_spinner_side_effect(event: str) -> Generator[None]:
            try:
                yield
                self._add_to_output_str(f"✓ {event}\n")
            except Exception:
                self._add_to_output_str(f"✗ {event}\n")
                raise

        self._output_str: str = ""
        self.input_mapping_callbacks: list[InputMappingCallback] = []

        mock_for(wait_for_enter).side_effect = _wait_for_enter_side_effect
        mock_for(str_input).side_effect = _str_input_side_effect
        mock_for(loading_spinner).side_effect = _loading_spinner_side_effect
        mock_for(display).side_effect = _display_side_effect

    def _add_to_output_str(self, s: str) -> None:
        self._output_str += s

    def output_str(self) -> str:
        return self._output_str

    def clear_output(self) -> None:
        self._output_str = ""


def user_io_fake() -> UserIOFake:
    return fake_for(UserIOFake)


def assert_displayed(expected: str) -> None:
    assert expected in user_io_fake().output_str(), dedent("""\
        Expected output was not displayed.
        Expected Output:
        ----------------
        {expected}
        ----------------
        Full Output:
        ----------------
        {full_output}
        ----------------
    """).format(expected=expected, full_output=user_io_fake().output_str())


def assert_displayed_exactly_once(expected: str) -> None:
    assert_displayed(expected)
    output = user_io_fake().output_str()
    expected_count = output.count(expected)
    assert expected_count == 1, (
        f"Expected `{expected}` to be displayed once but it was displayed {expected_count} times in the output: `{output}`"
    )


def assert_not_displayed(expected: str) -> None:
    assert expected not in user_io_fake().output_str()


def assert_displayed_in_order(*outputs: str) -> None:
    output = user_io_fake().output_str()
    for before, after in itertools.pairwise(outputs):
        try:
            before_index = output.index(before)
        except ValueError:
            pytest.fail(
                f"Expected the output `{before}` to appear before the output `{after}`, but `{before}` did not appear at all. Complete output: `{output}`"
            )
        try:
            after_index = output.index(after)
        except ValueError:
            pytest.fail(
                f"Expected the output `{before}` to appear before the output `{after}`, but `{after}` did not appear at all. Complete output: `{output}`"
            )
        assert before_index < after_index, (
            f"Expected the output `{before}` to appear before `{after}` in the output: `{output}`"
        )
