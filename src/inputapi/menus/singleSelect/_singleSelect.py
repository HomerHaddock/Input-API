from ...otherFunc import clearScreen as _clearScreen
from ...numerical.integer import newLineInt as _newLineInt
from ...strings import newLineStr as _newLineStr
import termcolor


def numericSerial(
    *args, clearOnLoad: bool = False, clearWhenDone: bool = False, title: str = "Menu"
) -> int:

    if clearOnLoad:
        _clearScreen.auto()

    if title != "":
        print(termcolor.colored(f"---{title}---", "black", "on_white"))

    # All serials will begin at 1 and increase by 1 every loop (Sorta like a factory)
    serial = 1
    options = []
    for arg in args:
        print(f"{serial}: {arg}")
        options.append(serial)
        serial += 1

    print()

    chosen = False
    while not chosen:
        user = _newLineInt("To select an option input the number assigned to it:")
        chosen = user in options

    if clearWhenDone:
        _clearScreen.auto()

    return user


def numericIndex(
    *args, clearOnLoad: bool = False, clearWhenDone: bool = False, title: str = "Menu"
) -> int:

    if clearOnLoad:
        _clearScreen.auto()

    if title != "":
        print(termcolor.colored(f"---{title}---", "black", "on_white"))

    # Instead of a serial number it will give it as an index
    index = 0
    options = []
    for arg in args:
        print(f"{index}: {arg}")
        options.append(index)
        index += 1

    print()

    chosen = False
    while not chosen:
        user = _newLineInt("To select an option input the number assigned to it:")
        chosen = user in options

    if clearWhenDone:
        _clearScreen.auto()

    return user


def alphabetical(
    *args, clearOnLoad: bool = False, clearWhenDone: bool = False, title: str = "Menu"
) -> str:

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
        print(termcolor.colored(f"---{title}---", "black", "on_white"))

    options = set()
    for arg in args:
        option = ""
        for i in index:
            option += letters[i]
        print(f"{option}: {arg}")
        index[-1] += 1
        if index[-1] >= 26:
            for i in range(len(index), 0, -1):
                if index[i - 1] >= 26 and i != 0:
                    index[i - 1] = 0
                    index[i - 2] += 1
            if index[0] >= 26:
                index[0] = 0
                index.insert(0, 0)
        options.add(option)

    print()

    chosen = False
    while not chosen:
        user = _newLineStr(
            "To select an option input the letters next to it:", 1, len(index), letters
        ).capitalize()
        chosen = user in options

    if clearWhenDone:
        _clearScreen.auto()

    return user


__all__ = ["numericSerial", "numericIndex", "alphabetical"]
