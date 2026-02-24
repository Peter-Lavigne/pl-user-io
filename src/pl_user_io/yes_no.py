from pl_user_io.display import display
from pl_user_io.str_input import str_input


def yes_no(question: str) -> bool:
    """Asks the user a yes/no question and returns their answer ("y" or "n") as a boolean."""
    response = str_input(f"{question} (y/n)")

    if response == "y":
        display()
        return True
    if response == "n":
        display()
        return False
    return yes_no(question)
