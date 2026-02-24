from pl_user_io.yes_no import yes_no


def assert_yes(question: str) -> None:
    assert yes_no(question), f"User indicated 'no' to the question: {question}"
