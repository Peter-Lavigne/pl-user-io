from pl_user_io.display import display
from pl_user_io.wait_for_enter import wait_for_enter


def task(instruction: str) -> None:
    display(instruction)
    wait_for_enter()
