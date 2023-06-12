from ... import strings as _strings
from ...otherFunc import clearScreen
import logging


def floatHandle(
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
    allowNeg: bool = True,
    min: float | int | None = None,
    max: float | int | None = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> float:
    if clearOnLoad:
        clearScreen.auto()

    allow = "0123456789."
    if allowNeg:
        allow += "-"

    minInput = 1
    maxInput = None
    if max is not None:
        maxInput = len(str(max))

    if request != "":
        print(request)

    validInput = False
    while validInput is not True:
        user = _strings.sameLineStr(
            ">", minLength=minInput, maxLength=maxInput, allowOnly=allow
        )
        if type(number:=floatHandle(user, allowNeg, min, max)) is float:
            user = number
            validInput = True

    if clearWhenDone:
        clearScreen.auto()

    return user


def sameLineFloat(
    request: str = "Decimal=",
    allowNeg: bool = True,
    min: float | int | None = None,
    max: float | int | None = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> float:
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
    while validInput is not True:
        user = _strings.sameLineStr(
            request, minLength=minInput, maxLength=maxInput, allowOnly=allow
        )
        if type(number:=floatHandle(user, allowNeg, min, max)) is float:
            user = number
            validInput = True

    if clearWhenDone:
        clearScreen.auto()

    return user


__all__ = ["newLineFloat", "sameLineFloat"]
