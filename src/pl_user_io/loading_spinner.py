from collections.abc import Generator
from contextlib import contextmanager

from pl_mocks_and_fakes import MockInUnitTests, MockReason
from rich import print as rprint
from rich import status
from rich.style import Style


@MockInUnitTests(MockReason.UNMITIGATED_SIDE_EFFECT)
@contextmanager
def loading_spinner(event: str) -> Generator[None]:
    s = status.Status(event, spinner="dots", spinner_style=Style(color="cyan"))
    s.start()
    try:
        yield
        rprint(f"[green]✓[/green] {event}")
    except Exception:
        rprint(f"[red]✗[/red] {event}")
        raise
    finally:
        s.stop()
