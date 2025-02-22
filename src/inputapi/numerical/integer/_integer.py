import logging as _logging
from ... import strings as _strings, otherFunc as _otherFunc


def _intHandle(
    input: str, allowNeg: bool, min: int | None, max: int | None
) -> int | bool:
    negCount: int = input.count("-")
    input: str = input.replace("-", "")
    input: str = "-" + input if negCount % 2 else input

    inputInt: int = int(input)

    if min is not None:
        if inputInt < min:
            _logging.warning("Number [%s] below minimum [%s]" % (input, min))
            return False

    if max is not None:
        if inputInt > max:
            _logging.warning("Number [%s] above maximum [%s]" % (input, max))
            return False

    return inputInt


def newLineInt(
    request: str = "Input an integer:",
    *,
    allowNeg: bool = True,
    min: int | None = None,
    max: int | None = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> int:
    """newLineInt requests an integer from the user on a newline

    Asks the user for an integer on the line below `request` then turns it into an integer
    what is returned is a valid integer with no errors.

    Args:
        request (str, optional): What you tell the user when requesting an integer. Defaults to "Input an integer:".
        allowNeg (bool, optional): Allows negative integers as input. Defaults to True.
        min (int | None, optional): The lowest number allowed (None means no min). Defaults to None.
        max (int | None, optional): The largest number allowed (None means no max). Defaults to None.
        clearOnLoad (bool, optional): Clears terminal before loading. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal after getting input. Defaults to False.

    Returns:
        int: The input given by the user
    """  # noqa: E501

    if clearOnLoad:
        _otherFunc.clearScreen.auto()

    display = ""
    if request != "":
        display = request

    allow = "0123456789"
    if allowNeg:
        allow += "-"

    minInput = 1
    maxInput = None
    if max is not None:
        maxInput = len(str(max))

    validInput = False
    while validInput is not True:
        user = _strings.sameLineStr(
            display + "\n>", minLength=minInput, maxLength=maxInput, allowOnly=allow
        )

        check = _intHandle(user, allowNeg, min, max)
        if not isinstance(check, bool):
            user = check
            validInput = True

    if clearWhenDone:
        _otherFunc.clearScreen.auto()

    return user  # type: ignore


def sameLineInt(
    request: str = "Integer=",
    *,
    allowNeg: bool = True,
    min: int | None = None,
    max: int | None = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> int:
    """sameLineInt requests an integer on the same line as `request`

    When asking for an integer the input will be on the same line as `request`
    This input is best suited for more compact input.

    Args:
        request (str, optional): What the user will see when requesting input. Defaults to "Integer=".
        allowNeg (bool, optional): Allows the user to enter a negative number. Defaults to True.
        min (int | None, optional): The minimum number to be inputed (There will be no min if it's None). Defaults to None.
        max (int | None, optional): The allowed maximum (if this is None there is no max). Defaults to None.
        clearOnLoad (bool, optional): Clears terminal before requesting input. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal when user gives valid input. Defaults to False.

    Returns:
        int: The input given from the user
    """  # noqa: E501
    if clearOnLoad:
        _otherFunc.clearScreen.auto()

    allow = "0123456789."
    if allowNeg:
        allow += "-"

    minInput = 1
    maxInput = None
    if max is not None:
        maxInput = len(str(max))

    validInput = False
    request = ">" if not request else request
    while validInput is not True:
        user = _strings.sameLineStr(
            request, minLength=minInput, maxLength=maxInput, allowOnly=allow
        )

        check = _intHandle(user, allowNeg, min, max)
        if not isinstance(check, bool):
            user = check
            validInput = True

    if clearWhenDone:
        _otherFunc.clearScreen.auto()

    return user  # type: ignore


__all__ = ["newLineInt", "sameLineInt"]
