from pl_user_io.display import display
from pl_user_io.int_input import int_input


def multiple_choice[T](question: str, options: list[tuple[str, T]]) -> T:
    display(f"{question}")
    for i, option in enumerate(options):
        display(f"{i + 1}. {option[0]}")
    try:
        choice = int_input(f"(1-{len(options)})")
        if choice < 1 or choice > len(options):
            raise IndexError
        result = options[choice - 1][1]
    except IndexError:
        display()
        return multiple_choice(question, options)
    else:
        display()
        return result
