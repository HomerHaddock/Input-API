from .. import clearScreen


def standard(*, clearOnLoad: bool = False, clearWhenDone: bool = False):
    """Pauses program until user presses ENTER.

    This function will pause the program until the user presses ENTER.
    This function will also clear the screen if specified.
    Note: This function will not display values

    Args:
        clearOnLoad (bool, optional): Clears terminal before pausing. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal after user presses ENTER. Defaults to False.
    """  # noqa: E501
    if clearOnLoad:
        clearScreen.auto()
    input("Press ENTER to continue:")
    if clearWhenDone:
        clearScreen.auto()


def showValue(*values, clearOnLoad: bool = False, clearWhenDone: bool = False):
    """showValue pauses program after displaying values.

    This function will pause the program after displaying values.
    Values are only positional arguments.

    Args:
        clearOnLoad (bool, optional): Clears terminal before pausing. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal when finished. Defaults to False.
    """  # noqa: E501
    if clearOnLoad:
        clearScreen.auto()
    print(*values, sep="\n")
    standard()
    if clearWhenDone:
        clearScreen.auto()


__all__ = ["standard", "showValue"]
