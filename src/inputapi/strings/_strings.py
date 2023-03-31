from ..otherFunc import clearScreen


def newLineStr(
    request: str = "Input a string:",
    minLength: int = 0,
    maxLength: int = None,
    allowOnly: str = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> str:

    if clearOnLoad:
        clearScreen.auto()

    if request != "":
        print(request)

    run = True
    while run == True:
        user = input(">")

        error = False
        if len(user) < minLength:
            error = True
            print(
                f"ERROR: Too few characters, minimum amount is [{minLength}] characters, you entered [{len(user)}]"
            )
        if len(user) > maxLength and maxLength != None:
            error = True
            print(
                f"ERROR: Too many characters, maximum amount is [{maxLength}] characters, you entered [{len(user)}]"
            )
        if allowOnly != None:
            for x in user:
                if x not in allowOnly:
                    error = True
                    print(
                        f"ERROR: Invalid character [{x}], to ensure the program runs correctly please enter only these characters [{', '.join(x for  x in allowOnly)}]"
                    )
                    break
        if error == False:
            run = False

    if clearWhenDone:
        clearScreen.auto()

    return user


def sameLineStr(
    request: str = "String=",
    minLength: int = 0,
    maxLength: int = None,
    allowOnly: str = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
):
    if clearOnLoad:
        clearScreen.auto()

    run = True
    while run:
        user = input(request)

        error = False
        if len(user) < minLength:
            error = True
            print(
                f"ERROR: Too few characters, minimum amount is [{minLength}] characters, you entered [{len(user)}]"
            )
        if maxLength != None:
            if len(user) > maxLength:
                error = True
                print(
                    f"ERROR: Too many characters, maximum amount is [{maxLength}] characters, you entered [{len(user)}]"
                )
        if allowOnly != None:
            for x in user:
                if x not in allowOnly:
                    error = True
                    print(
                        f"ERROR: Invalid character [{x}], to ensure the program runs correctly please enter only these characters [{', '.join(x for  x in allowOnly)}]"
                    )
                    break
        if error == False:
            run = False

    return user


__all__ = ["newLineStr", "sameLineStr"]
