from typing import Generator, Sequence

from ...numerical.integer import newLineInt as _newLineInt
from ...otherFunc import clearScreen as _clearScreen
from ...strings import newLineStr as _newLineStr


def numericSerial(
    *args,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
    title: str = "Menu",
) -> int:
    """A menu for the single selection of a user

    A list of options supplied through *args for the user to select.
    Every option is given a number from 1 to length of *args.
    What is returned is what the user selected.

    Args:
        clearOnLoad (bool, optional): Clears terminal before displaying. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal when finished. Defaults to False.
        title (str, optional): The title displayed for the menu. Defaults to "Menu".

    Returns:
        int: What the user selected
    """  # noqa: E501

    if len(args) == 0:
        raise SyntaxError("*args has [0] value(s), [1] or more values is needed.")

    if clearOnLoad:
        _clearScreen.auto()

    display = "\u001b[30m\u001b[47m---%s---\u001b[0m" % title if title != "" else ""

    # All serials will begin at 1 and increase by 1 every loop (Sorta like a factory)
    serial = 1
    for arg in args:
        display += "\n%s: %s" % (serial, arg)
        serial += 1

    display += "\n"

    chosen = False
    while not chosen:
        user = _newLineInt(
            display + "\nTo select an option input the number assigned to it:"
        )
        chosen = user >= 1 and user <= serial - 1

    if clearWhenDone:
        _clearScreen.auto()

    return user  # type: ignore


def numericIndex(
    *args, clearOnLoad: bool = False, clearWhenDone: bool = False, title: str = "Menu"
) -> int:
    """numericIndex is a neumeric menu starting at 0

    In similar fashion as menu and numericSerial this is a number based selection menu.
    All options are given a number between 0 and length of *args minus 1.
    What is returned is the number given to the option.

    Args:
        clearOnLoad (bool, optional): Clears terminal before displaying options. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal when finished. Defaults to False.
        title (str, optional): The title to be displayed. Defaults to "Menu".

    Returns:
        int: The number to be assigned to the selected option
    """  # noqa: E501

    if clearOnLoad:
        _clearScreen.auto()

    display = "\u001b[30m\u001b[47m---%s---\u001b[0m" % title if title else ""

    # Instead of a serial number it will give it as an index
    index = 0
    for arg in args:
        display += "\n%s: %s" % (index, arg)
        index += 1

    display += "\n"

    chosen = False
    while not chosen:
        user = _newLineInt(
            display + "\nTo select an option input the number assigned to it:"
        )
        chosen = user >= 0 and user <= index

    if clearWhenDone:
        _clearScreen.auto()

    return user  # type: ignore


def _generateAlphabetical(letters: Sequence[str]) -> Generator[str, None, None]:
    length = len(letters)
    index = [0]
    while True:
        yield "".join([letters[i] for i in index])
        index[-1] += 1
        for i in range(len(index) - 1, 0, -1):
            if index[i] >= length:
                index[i] = 0
                index[i - 1] += 1
        if index[0] >= length:
            index[0] = 0
            index.insert(0, 0)


def alphabetical(
    *args, clearOnLoad: bool = False, clearWhenDone: bool = False, title: str = "Menu"
) -> str:
    """alphabetical is a menu that assigns options with the Modern Latin Alphabet

    This menu has the weird property of using only 26 characters from the Modern Latin Alphabet.
    The characters are from A to Z and don't reach the limit of 26 options (Though too many options is ridiculous).
    What is returned is the characters assigned to the option.

    Args:
        clearOnLoad (bool, optional): Clears terminal before starting. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal after getting valid input. Defaults to False.
        title (str, optional): The name/title of the menu. Defaults to "Menu".

    Raises:
        ValueError: This will only happen if the assignment system for options has a heart attack and gives a duplicate.

    Returns:
        str: The characters assigned to an option.
    """  # noqa: E501

    if clearOnLoad:
        _clearScreen.auto()

    # Len is 26 btw
    letters: tuple = (
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    )

    display = ""
    if title != "":
        display = "\u001b[30m\u001b[47m---%s---\u001b[0m" % title

    options: list[str] = []
    generator = _generateAlphabetical(letters)
    for arg in args:
        option = next(generator)
        display += "\n%s: %s" % (option, arg)
        if option in options:
            raise ValueError("Generated option was given pre-existant indentifier")
        options.append(option)
    generator.close()

    display += "\n"

    chosen = False
    while not chosen:
        user = _newLineStr(
            display + "\nTo select an option input the letters next to it:",
            minLength=1,
            maxLength=max([len(i) for i in options]),
        ).upper()
        chosen = user in options

    if clearWhenDone:
        _clearScreen.auto()

    return user  # type: ignore


__all__ = ["numericSerial", "numericIndex", "alphabetical"]
