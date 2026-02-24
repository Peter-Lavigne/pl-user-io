from pl_mocks_and_fakes import (
    HUMAN_INTERACTION_MOCK_REASONS,
    MockInUnitTests,
)

StrInputParam = str
StrInputResponse = str


@MockInUnitTests(*HUMAN_INTERACTION_MOCK_REASONS)
def str_input(prompt: StrInputParam) -> StrInputResponse:
    return input(prompt + " ")
