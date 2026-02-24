from pl_user_io.str_input import str_input
from tests.constants import PYTEST_INTEGRATION_MARKER

pytestmark = PYTEST_INTEGRATION_MARKER


def test_asks_for_user_input() -> None:
    result = str_input("Enter 'test':")

    assert result == "test"


def test_there_is_a_space_between_prompt_and_input() -> None:
    result = str_input(
        "If there is a space between this prompt and your input, enter 'yes'. Otherwise, enter 'no'."
    )

    assert result == "yes"
