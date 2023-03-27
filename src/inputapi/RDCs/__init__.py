from ..menus import singleSelect
from ..numericals.float import newLineFloat, sameLineFloat
from math import pi


def newLineRDC(clearOnLoad: bool = False, clearWhenDone: bool = False) -> float:
    length = newLineFloat("RDC:")
    chosen = singleSelect.numericSerial(
        "Radius",
        "Diameter",
        "Circumference",
        clearOnLoad=clearOnLoad,
        clearWhenDone=clearWhenDone,
        title="RDC",
    )

    if chosen == 1:
        return length
    elif chosen == 2:
        return length / 2
    elif chosen == 3:
        return length / (2 * pi)


def sameLineRDC(clearOnLoad: bool = False, clearWhenDone: bool = False):
    length = sameLineFloat("RDC=")
    chosen = singleSelect.numericSerial(
        "Radius",
        "Diameter",
        "Circumference",
        clearOnLoad=clearOnLoad,
        clearWhenDone=clearWhenDone,
        title="RDC",
    )

    if chosen == 1:
        return length
    elif chosen == 2:
        return length / 2
    elif chosen == 3:
        return length / (2 * pi)


def RDC(length: float, clearOnLoad: bool = False, clearWhenDone: bool = False) -> float:
    chosen = singleSelect.numericSerial(
        "Radius",
        "Diameter",
        "Circumference",
        clearOnLoad=clearOnLoad,
        clearWhenDone=clearWhenDone,
        title="RDC",
    )

    if chosen == 1:
        return length
    elif chosen == 2:
        return length / 2
    elif chosen == 3:
        return length / (2 * pi)


__all__ = ["newLineRDC", "sameLineRDC", "RDC"]
