from pl_user_io.multiple_choice import multiple_choice
from pl_user_io.testing.assertions import (
    assert_multiple_choice_displayed,
    assert_multiple_choice_not_displayed,
)
from pl_user_io.testing.helpers import options_for_multiple_choice
from pl_user_io.testing.stubs import (
    stub_multiple_choice,
)


def test_stub_multiple_choice() -> None:
    stub_multiple_choice("Choose an option", "Second option")

    result = multiple_choice(
        "Choose an option",
        [("First option", "x"), ("Second option", "y"), ("Third option", "z")],
    )

    assert result == "y"


def test_assert_multiple_choice_displayed() -> None:
    stub_multiple_choice("Choose an option", "Second option")

    multiple_choice(
        "Choose an option",
        [
            ("First option", "a"),
            ("Second option", "b"),
        ],
    )

    assert_multiple_choice_displayed("Choose an option")


def test_assert_multiple_choice_not_displayed() -> None:
    stub_multiple_choice("Choose ONE option", "Second option")

    multiple_choice(
        "Choose ONE option",
        [
            ("First option", "a"),
            ("Second option", "b"),
        ],
    )

    assert_multiple_choice_not_displayed("Choose an option")


def test_options_for_multiple_choice() -> None:
    stub_multiple_choice("Choose an option", "Second option")

    multiple_choice(
        "Choose an option",
        [
            ("First option", "a"),
            ("Second option", "b"),
        ],
    )
    options = options_for_multiple_choice("Choose an option")

    assert options == ["First option", "Second option"]


def test_options_for_multiple_choice__index() -> None:
    stub_multiple_choice("Choose an option", "First option")
    stub_multiple_choice("Choose an option", "Third option")
    stub_multiple_choice("Choose an option", "Fifth option")

    multiple_choice(
        "Choose an option",
        [
            ("First option", "a"),
            ("Second option", "b"),
        ],
    )
    multiple_choice(
        "Choose an option",
        [
            ("Third option", "c"),
            ("Fourth option", "d"),
        ],
    )
    multiple_choice(
        "Choose an option",
        [
            ("Fifth option", "e"),
            ("Sixth option", "f"),
        ],
    )
    options = options_for_multiple_choice("Choose an option", index=1)

    assert options == ["Third option", "Fourth option"]
