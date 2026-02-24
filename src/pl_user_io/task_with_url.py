from pl_user_io.open_url import open_url
from pl_user_io.pause_and_read import pause_and_read
from pl_user_io.wait_for_enter import wait_for_enter


def task_with_url(instruction: str, url_to_open: str) -> None:
    pause_and_read(instruction)
    # I ran into an issue on mac startup where this was trying to open chrome, not firefox.
    # I fixed it by starting firefox on device startup.
    open_url(url_to_open)
    wait_for_enter()
