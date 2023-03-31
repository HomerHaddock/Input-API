from .. import clearScreen


def standard(clearOnLoad: bool = False, clearWhenDone: bool = False):
    if clearOnLoad:
        clearScreen.auto()
    input("Press ENTER to continue:")
    if clearWhenDone:
        clearScreen.auto()


def showValue(*values, clearOnLoad: bool = False, clearWhenDone: bool = False):
    if clearOnLoad:
        clearScreen.auto()
    print(*values)
    standard()
    if clearWhenDone:
        clearScreen.auto()


__all__ = ["standard", "showValue"]
