from ... import strings as _strings
from ...otherFunc import clearScreen
import logging


def _floatHandle(
    input: str, allowNeg: bool, min: float | None, max: float | None
) -> float | bool:  # noqa: E501
    # Negative handler (e.g. --2 -> 2 or 2- -> -2)
    negCount = input.count("-")
    input = input.replace("-", "")
    input = "-" + input if negCount % 2 else input

    # Decimal handler (e.g. 2.2.2 -> 2.220 or 2 -> 2.0)
    inputSplit = input.split(".")
    inputSplit.insert(1, ".")
    inputSplit.append("0")
    input = "".join(inputSplit)

    inputFloat = float(input)

    if min is not None:
        if inputFloat < min:
            logging.warning("Number [%s] is below minimum [%s]" % (input, min))
            return False

    if max is not None:
        if inputFloat > max:
            logging.warning("Number [%s] is above maximum [%s]" % (input, max))
            return False

    return inputFloat


def newLineFloat(
    request: str = "Input an floating point number (Decimal):",
    *,
    allowNeg: bool = True,
    min: float | int | None = None,
    max: float | int | None = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> float:
    """newLineFloat inputs floating point number on a newline.

    This input asks for a floating point number on the line below the request string.
    It will ensure that what is returned is a valid number with no errors.

    Args:
        request (str, optional): The request or question of the values purpose. Defaults to "Input an floating point number (Decimal):".
        allowNeg (bool, optional): Allows negative numbers without messing with min. Defaults to True.
        min (float | int | None, optional): The lowest number that can be given (None means no min). Defaults to None.
        max (float | int | None, optional): The highest number allowed (None means no max). Defaults to None.
        clearOnLoad (bool, optional): Clears terminal before requesting input. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal after getting input. Defaults to False.

    Returns:
        float: The number that the user gave
    """  # noqa: E501

    if clearOnLoad:
        clearScreen.auto()

    allow = "0123456789."
    if allowNeg:
        allow += "-"

    minInput = 1
    maxInput = None
    if max is not None:
        maxInput = len(str(max))

    display = ""
    if request != "":
        display = request

    validInput = False
    while validInput is not True:
        user = _strings.sameLineStr(
            display + "\n>", minLength=minInput, maxLength=maxInput, allowOnly=allow
        )

        check = _floatHandle(user, allowNeg, min, max)
        if isinstance(check, float):
            user = check
            validInput = True

    if clearWhenDone:
        clearScreen.auto()

    return user


def sameLineFloat(
    request: str = "Decimal=",
    *,
    allowNeg: bool = True,
    min: float | int | None = None,
    max: float | int | None = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> float:
    """sameLineFloat asks the user for floating point number on the same line as request

    This input works similar to newLineFloat but instead of having the input be on a new line
    it will instead input on the same line as request for more compact input(s).

    Args:
        request (str, optional): The output to the user on what to input. Defaults to "Decimal=".
        allowNeg (bool, optional): Allows negative numbers as input. Defaults to True.
        min (float | int | None, optional): The lowest number allowed for input (None is no min). Defaults to None.
        max (float | int | None, optional): The highest number allowed (None means no max). Defaults to None.
        clearOnLoad (bool, optional): Clears terminal before requesting input. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal after getting input. Defaults to False.

    Returns:
        float: The input the user gave
    """  # noqa: E501

    if clearOnLoad:
        clearScreen.auto()

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

        check = _floatHandle(user, allowNeg, min, max)
        if isinstance(check, float):
            user = check
            validInput = True

    if clearWhenDone:
        clearScreen.auto()

    return user


__all__ = ["newLineFloat", "sameLineFloat"]
