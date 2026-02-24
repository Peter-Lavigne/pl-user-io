from datetime import timedelta

from pl_mocks_and_fakes import MockInUnitTests, MockReason

from pl_user_io.delay import delay


@MockInUnitTests(MockReason.UNINVESTIGATED)
def pause_to_read(text: str) -> None:
    """
    Pauses for a length of time proportional to the length of the text.

    You probably want to use `pause_and_read`, instead, which also prints the text.
    """
    chars_per_second = 30
    min_read_time = 1
    read_time = max(len(text) / chars_per_second, min_read_time)
    delay(timedelta(seconds=read_time))
