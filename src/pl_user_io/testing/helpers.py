import re

import pytest

from pl_user_io.testing.user_io_fake import user_io_fake

type Question = str
type Answer = str


def all_instances_of_question(question: Question) -> list[str]:
    number_select_regex = r"\(1-\d+\)"
    minimum_any_characters_regex = r".+?"
    return re.findall(
        rf"{re.escape(question)}\n{minimum_any_characters_regex}\n{number_select_regex}",
        user_io_fake().output_str(),
        re.DOTALL,
    )


def options_for_multiple_choice(question: str, index: int = 0) -> list[str]:
    result = all_instances_of_question(question)
    if len(result) == 0:
        pytest.fail(f"Multiple choice question not found: `{question}`")
    return [line.split(" ", maxsplit=1)[1] for line in result[index].split("\n")[1:-1]]
