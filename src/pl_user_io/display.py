from pl_mocks_and_fakes import (
    MockInUnitTests,
    MockReason,
)


@MockInUnitTests(MockReason.UNMITIGATED_SIDE_EFFECT)
def display(*values: object, end: str | None = "\n", flush: bool = False) -> None:
    print(*values, end=end, flush=flush)
