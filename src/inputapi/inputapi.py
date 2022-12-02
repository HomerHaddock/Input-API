import math
import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def verifyInt(number: str):

    if number.count("-") % 2 == 1:
        isNeg = True
    else:
        isNeg = False

    isInt = True
    for x in number:
        if x not in "-0123456789":
            isInt = False

    return [isInt, isNeg]


def newLineInt(request: str = "Input an integer:"):
    if request != "":
        print(request)

    isInt = False
    while not isInt:
        userIn = input(">")
        resp = verifyInt(userIn)
        isInt = resp[0]
    if len(userIn) >= 1:
        userInt = int(userIn.replace("-", ""))

    if resp[1]:
        userInt *= -1

    return userInt


def yesNo(request: str):
    print(request)

    actualResponse = False
    while actualResponse != True:
        query = input("[Y/n]:")
        if query.lower() in {"y", "n"}:
            actualResponse = True

    print()

    return query.lower() == "y"


def menu(*args, clearOnLoad: bool = False, clearWhenDone: bool = False, title: str = "Menu"):
    print()

    if clearOnLoad:
        clearScreen()

    if title != "":
        print(f"\033[1;30;47m---{title}---\033[0;0m")

    # All serials will begin at 1 and increase by 1 every loop (Sorta like a factory)
    serial = 1
    options = []
    for arg in args:
        print(f"{serial}: {arg}")
        options.append(serial)
        serial += 1


    print()

    chosen = False
    while not chosen:
        user = newLineInt("To select an option input the number assigned to it:")
        chosen = user in options

    if clearWhenDone:
        clearScreen()

    return user


def RDC(length: float):
    chosen = menu("Radius", "Diameter", "Circumference", title="RDC")

    if chosen == 1:
        return length
    elif chosen == 2:
        return length / 2
    elif chosen == 3:
        return length / (2 * math.pi)


def verifyFlt(number: str):

    if number.count("-") % 2 == 1:
        isNeg = True
    else:
        isNeg = False

    isFlt = True
    for x in number:
        if x not in "-0123456789.":
            isFlt = False

    isDblPrd = False
    if number.count(".") >= 2:
        isFlt = False
        isDblPrd = True

    if len(number) == 0:
        isFlt = False

    return [isFlt, isNeg, isDblPrd]


def newLineFloat(request: str = "Input an floating point number (Decimal):"):

    if request != "":
        print(request)

    isFlt = False
    while not isFlt:
        user = input(">")
        resp = verifyFlt(user)
        if resp[2]:
            userLst = user.split(".")
            userLst.insert(1, ".")
            user = "".join(userLst)
            resp[0] = True
        isFlt = resp[0]

    userFlt = float(user.replace("-", ""))

    if resp[1]:
        userFlt *= -1

    return userFlt


def pause():
    input("Press ENTER to continue:")
