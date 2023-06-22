from ...otherFunc import clearScreen as _clearScreen
from ...numerical.integer import newLineInt as _newLineInt
from ...strings import newLineStr as _newLineStr


def numericSerial(
    *args,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
    title: str = "Menu"
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
        raise SyntaxError('*args has [0] value(s), [1] or more values is needed.')

    if clearOnLoad:
        _clearScreen.auto()

    if title != "":
        print("\u001b[30m\u001b[47m---%s---\u001b[0m" % title)

    # All serials will begin at 1 and increase by 1 every loop (Sorta like a factory)
    serial = 1
    options = []
    for arg in args:
        print("%s: %s" % (serial, arg))
        options.append(serial)
        serial += 1

    print()

    chosen = False
    while not chosen:
        user = _newLineInt(
            "To select an option input the number assigned to it:")
        chosen = user in options

    if clearWhenDone:
        _clearScreen.auto()

    return user  # type: ignore


def numericIndex(
    *args,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
    title: str = "Menu"
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

    if title != "":
        print("\u001b[30m\u001b[47m---%s---\u001b[0m" % title)

    # Instead of a serial number it will give it as an index
    index = 0
    options = []
    for arg in args:
        print("%s: %s" % (index, arg))
        options.append(index)
        index += 1

    print()

    chosen = False
    while not chosen:
        user = _newLineInt(
            "To select an option input the number assigned to it:")
        chosen = user in options

    if clearWhenDone:
        _clearScreen.auto()

    return user  # type: ignore


def alphabetical(
    *args,
    clearOnLoad: bool = False, 
    clearWhenDone: bool = False,
    title: str = "Menu"
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
    letters = (
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
    index = [0]

    if title != "":
        print("\u001b[30m\u001b[47m---%s---\u001b[0m" % title)

    options = []
    for arg in args:
        option = ""
        for i in index:
            option += letters[i]
        print("%s: %s" % (option, arg))
        index[-1] += 1
        if index[-1] >= 26:
            while max(index) >= 26:
                if index[0] >= 26:
                    index[0] = 0
                    index.insert(0, 0)
                for i,j in enumerate(index):
                    if j >= 26:
                        index[i] = 0
                        index[i-1] += 1
        if option in options:
            raise ValueError('Generated option was given pre-existant indentifier')
        options.append(option)

    print()

    chosen = False
    while not chosen:
        user = _newLineStr(
            "To select an option input the letters next to it:",
            minLength=1,
            maxLength=len(letters),
            allowOnly=''.join(letters) + ''.join([x.lower() for x in letters]),
        ).upper()
        chosen = user in options

    if clearWhenDone:
        _clearScreen.auto()

    return user  # type: ignore


__all__ = ["numericSerial", "numericIndex", "alphabetical"]
