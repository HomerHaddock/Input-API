import logging
from ... import strings as _strings, otherFunc as _otherFunc


def intStat(number: str) -> list[int]:
    neg = number.count("-")
    return [neg]


def newLineInt(
    request: str = "Input an integer:",
    *,
    allowNeg: bool = True,
    min: int | None = None,
    max: int | None = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
):
    if clearOnLoad:
        _otherFunc.clearScreen.auto()

    if request != "":
        print(request)

    allow = "0123456789"
    if allowNeg:
        allow += "-"

    minInput = 1
    maxInput = None
    if max is not None:
        maxInput = len(str(max))

    followsMin = False
    followsMax = False
    followsNeg = False
    while not (followsMin and followsMax and followsNeg):
        user = _strings.sameLineStr(
            ">", minLength=minInput, maxLength=maxInput, allowOnly=allow
        )
        stat = intStat(user)
        user.replace("-", "")
        if stat[0] % 2 == 1:
            user = "-" + user
        user = int(user)
        if min is not None:
            if user < min:
                logging.warning(f"Number [{user}] below minimum [{min}]")
                continue
        followsMin = True
        if max is not None:
            if user > max:
                logging.warning(f"Number [{user}] above maximum [{max}]")
                continue
        followsMax = True
        if stat[0] % 2 == 1:
            if not allowNeg:
                logging.warning(
                    f"Number [{user}] is negative, negative numbers are disabled for this input"  # noqa: E501
                )
                continue
        followsNeg = True

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
    if clearOnLoad:
        _otherFunc.clearScreen.auto()

    allow = "0123456789."
    if allowNeg:
        allow += "-"

    minInput = 1
    maxInput = None
    if max is not None:
        maxInput = len(str(max))

    followsMin = False
    followsMax = False
    followsNeg = False
    while not followsMin or not followsMax or not followsNeg:
        user = _strings.sameLineStr(
            ">", minLength=minInput, maxLength=maxInput, allowOnly=allow
        )
        stat = intStat(user)
        user.replace("-", "")
        if stat[0] % 2 == 1:
            user = "-" + user
        user = int(user)
        if min is not None:
            if user < min:
                logging.warning(f"Number [{user}] below minimum [{min}]")
                continue
        followsMin = True
        if max is not None:
            if user > max:
                logging.warning(f"Number [{user}] above maximum [{max}]")
                continue
        followsMax = True
        if stat[0] % 2 == 1:
            if not allowNeg:
                logging.warning(
                    f"Number [{user}] is negative, negative numbers are disabled for this input"  # noqa: E501
                )
                continue
        followsNeg = True

    if clearWhenDone:
        _otherFunc.clearScreen.auto()

    return user  # type: ignore


__add__ = ["newLineInt", "sameLineInt", "intStat"]
