from ... import strings as _strings
from ...otherFunc import clearScreen


def floatStat(number: str) -> tuple[int, int]:
    neg = number.count("-")
    point = number.count(".")
    return (neg, point)


def newLineFloat(
    request: str = "Input an floating point number (Decimal):",
    allowNeg: bool = True,
    min: float = None,
    max: float = None,
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
    if max != None:
        maxInput = len(str(max))

    if request != "":
        print(request)

    followsMin = False
    followsMax = False
    followsNeg = False
    while not followsMin or not followsMax or not followsNeg:
        user = _strings.sameLineStr(">", minInput, maxInput, allow)
        stat = floatStat(user)
        user.replace("-", "")
        if stat[0] % 2 == 1:
            user = "-" + user
        if stat[1] % 2 == 1:
            split = user.split(".")
            split.insert(1, ".")
            user = "".join(split)
        user = float(user)
        if min != None:
            if user < min:
                print(f"ERROR: Number [{user}] below minimum [{min}]")
                continue
        followsMin = True
        if max != None:
            if user > max:
                print(f"ERROR: Number [{user}] above maximum [{max}]")
                continue
        followsMax = True
        if stat[0] % 2 == 1:
            if not allowNeg:
                print(
                    f"ERROR: Number [{user}] is negative, negative numbers are disabled for this input"
                )
                continue
        followsNeg = True

    if clearWhenDone:
        clearScreen.auto()

    return user


def sameLineFloat(
    request: str = "Decimal=",
    allowNeg: bool = True,
    min: float = None,
    max: float = None,
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
    if max != None:
        maxInput = len(str(max))

    followsMin = False
    followsMax = False
    followsNeg = False
    while not followsMin or not followsMax or not followsNeg:
        user = _strings.sameLineStr(request, minInput, maxInput, allow)
        stat = floatStat(user)
        user.replace("-", "")
        if stat[0] % 2 == 1:
            user = "-" + user
        if stat[1] > 1:
            split = user.split(".")
            split.insert(1, ".")
            user = "".join(split)
        user = float(user)
        if min != None:
            if user < min:
                print(f"ERROR: Number [{user}] below minimum [{min}]")
                continue
        followsMin = True
        if max != None:
            if user > max:
                print(f"ERROR: Number [{user}] above maximum [{max}]")
                continue
        followsMax = True
        if stat[0] % 2 == 1:
            if not allowNeg:
                print(
                    f"ERROR: Number [{user}] is negative, negative numbers are disabled for this input"
                )
                continue
        followsNeg = True

    if clearWhenDone:
        clearScreen.auto()

    return user


__all__ = ["floatStat", "newLineFloat", "sameLineFloat"]
