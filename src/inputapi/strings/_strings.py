import logging

from ..otherFunc import clearScreen


def allowedDisplayHandler(allowOnly: str) -> str:
    length: int = len(allowOnly)
    allowOnlyList: list[str] = list(allowOnly)

    if length < 20:
        string = "%s" % (allowOnlyList)
        return string.replace("[", "").replace("]", "")
    elif length > 25:
        string = "%s ... %s" % (allowOnlyList[:15], allowOnlyList[-5:])
        return string.replace("[", "").replace("]", "")
    else:
        string = "%s ... %s" % (allowOnlyList[:15], allowOnlyList[-1])
        return string.replace("[", "").replace("]", "")


def allowOnlyIterate(char: str, allowed: str) -> bool:
    if char not in allowed:
        logging.warning(
            "Input has invalid character [%s], allowed characters are [%s]"
            % (char, allowedDisplayHandler(allowed))  # noqa: E501
        )
        return False
    return True


def stringValidationCheck(
    input: str,
    minLength: int = 0,
    maxLength: int | None = None,
    allowOnly: str | None = None,
) -> bool:
    length: int = len(input)

    message: dict[str, int | str] = dict()

    if maxLength:
        if length > maxLength:
            message["limit"] = maxLength
            message["boundaryHint"] = "less"
            message["enteredLength"] = length
    if minLength:
        if length < minLength:
            message["limit"] = minLength
            message["boundaryHint"] = "more"
            message["enteredLength"] = length

    if len(message):
        logging.warning(
            "Input requires [%(limit)s] characters or %(boundaryHint)s, you entered [%(enteredLength)s] characters"  # noqa: E501
            % message
        )
        return False

    allValid = True
    if allowOnly:
        for x in input:
            valid = allowOnlyIterate(x, allowOnly)
            allValid = valid and allValid
            if not allValid:
                break

    return allValid


def newLineStr(
    request: str = "Input a string:",
    *,
    minLength: int = 0,
    maxLength: int | None = None,
    allowOnly: str | None = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> str:
    if clearOnLoad:
        clearScreen.auto()

    if request != "":
        request += "\n>"
    else:
        request = ">"

    run = True
    while run:
        user = input(request)

        valid = stringValidationCheck(user, minLength, maxLength, allowOnly)
        if valid is True:
            run = False

    if clearWhenDone:
        clearScreen.auto()

    return user  # type: ignore


def sameLineStr(
    request: str = "String=",
    *,
    minLength: int = 0,
    maxLength: int | None = None,
    allowOnly: str | None = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
):
    if clearOnLoad:
        clearScreen.auto()

    run = True
    while run:
        user = input(request)

        valid = stringValidationCheck(user, minLength, maxLength, allowOnly)
        if valid is True:
            run = False
        else:
            continue

    if clearWhenDone:
        clearScreen.auto()

    return user  # type: ignore


__all__ = ["newLineStr", "sameLineStr"]
