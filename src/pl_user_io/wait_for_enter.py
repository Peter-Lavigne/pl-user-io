from pl_mocks_and_fakes import (
    HUMAN_INTERACTION_MOCK_REASONS,
    MockInUnitTests,
)

from pl_user_io.display import display
from pl_user_io.str_input import str_input

WAIT_FOR_ENTER_TEXT = "Press Enter to continue:"


@MockInUnitTests(*HUMAN_INTERACTION_MOCK_REASONS)
def wait_for_enter() -> None:
    str_input(WAIT_FOR_ENTER_TEXT)
    # `input` calls add a trailing newline, so we need to remove it
    ansi_code_for_up_one_line = "\033[1A"
    ansi_code_for_clear_line = "\033[K"
    display(
        f"{ansi_code_for_up_one_line}{ansi_code_for_clear_line}{WAIT_FOR_ENTER_TEXT} ✓\n"
    )
