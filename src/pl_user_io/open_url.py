import subprocess
from pathlib import Path

from pl_mocks_and_fakes import MockInUnitTests, MockReason

FIREFOX_ABSOLUTE_PATH = Path("/snap/bin/firefox")


@MockInUnitTests(MockReason.UNINVESTIGATED)
def open_url(url: str) -> None:
    # Using run_program hangs until you quit the browser, which is not what we want. We just want to open the URL and move on.
    subprocess.Popen(
        [FIREFOX_ABSOLUTE_PATH, url],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
