from pl_user_io.yes_no import yes_no


def assert_no(question: str) -> None:
    assert not yes_no(question), f"User indicated 'yes' to the question: {question}"
