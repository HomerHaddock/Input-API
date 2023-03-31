from ... import strings as _strings, otherFunc as _otherFunc


def intStat(number: str) -> tuple[int]:
    neg = number.count("-")
    return [neg]


def newLineInt(
    request: str = "Input an integer:",
    allowNeg: bool = True,
    min: int = None,
    max: int = None,
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
    if max != None:
        maxInput = len(str(max))

    followsMin = False
    followsMax = False
    followsNeg = False
    while not (followsMin and followsMax and followsNeg):
        user = _strings.sameLineStr(">", minInput, maxInput, allow)
        stat = intStat(user)
        user.replace("-", "")
        if stat[0] % 2 == 1:
            user = "-" + user
        user = int(user)
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
        _otherFunc.clearScreen.auto()

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
        _otherFunc.clearScreen.auto()

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
        stat = intStat(user)
        user.replace("-", "")
        if stat[0] % 2 == 1:
            user = "-" + user
        user = int(user)
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
        _otherFunc.clearScreen.auto()

    return user


__add__ = ["newLineInt", "sameLineInt", "intStat"]
