import logging
from ... import strings as _strings, otherFunc as _otherFunc

def intHandle(input:str, allowNeg:bool, min:int|None, max:int|None) -> int|bool:
    negCount:int = input.count('-')
    input:str = input.replace('-', "")
    input:str = '-' + input if negCount % 2 else input

    inputInt:int = int(input)
    
    if min:
        if inputInt < min:
            logging.warning("Number [%s] below minimum [%s]" % (input, min))
            return False
    
    if max:
        if inputInt > max:
            logging.warning("Number [%s] above maximum [%s]" % (input, max))
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

    validInput = False
    while validInput is not True:
        user = _strings.sameLineStr(
            ">", minLength=minInput, maxLength=maxInput, allowOnly=allow
        )
        
        if type(result:=intHandle(user, allowNeg, min, max)) is int:
            user = result
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
    while validInput is not True:
        user = _strings.sameLineStr(
            ">", minLength=minInput, maxLength=maxInput, allowOnly=allow
        )
        
        if type(result:=intHandle(user, allowNeg, min, max)) is int:
            user = result
            validInput = True

    if clearWhenDone:
        _otherFunc.clearScreen.auto()

    return user  # type: ignore


__add__ = ["newLineInt", "sameLineInt"]
