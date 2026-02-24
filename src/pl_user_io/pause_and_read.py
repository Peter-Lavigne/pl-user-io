from pl_user_io.display import display
from pl_user_io.pause_to_read import pause_to_read


def pause_and_read(text: str) -> None:
    display(text)
    pause_to_read(text)
