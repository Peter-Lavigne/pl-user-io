from pl_user_io.str_input import str_input


def int_input(question: str) -> int:
    response = str_input(question)
    try:
        return int(response)
    except ValueError:
        return int_input(question)
