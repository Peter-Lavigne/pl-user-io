from collections.abc import Callable
from typing import Any, TypeVar

import pytest
from pl_mocks_and_fakes import create_fakes, initialize_mocks

import pl_user_io
import tests
from tests.constants import (
    PYTEST_INTEGRATION_TEST_MARKERS,
)

F = TypeVar("F", bound=Callable[..., Any])


def with_pytestmarks(*marks: pytest.MarkDecorator) -> Callable[[F], F]:
    """Apply the given pytest marks to a test function."""

    def decorator(func: F) -> F:
        func.__setattr__("pytestmark", list(marks))
        return func

    return decorator


def pytest_runtest_setup(item: pytest.Item) -> None:
    def _is_integration_test() -> bool:
        return any(
            marker.name in [m.name for m in PYTEST_INTEGRATION_TEST_MARKERS]
            for marker in item.iter_markers()
        )

    def _mock_code_for_unit_tests() -> None:
        if not _is_integration_test():
            initialize_mocks(pl_user_io)
            create_fakes(tests)

    _mock_code_for_unit_tests()
