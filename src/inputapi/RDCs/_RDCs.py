from ..menus import singleSelect as _singleSelect
from ..numerical.float import (
    newLineFloat as _newLineFloat,
    sameLineFloat as _sameLineFloat,
)
from math import pi as _pi


def newLineRDC(clearOnLoad: bool = False, clearWhenDone: bool = False) -> float:
    length = _newLineFloat("RDC:")
    chosen = _singleSelect.numericSerial(
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
        return length / (2 * _pi)


def sameLineRDC(clearOnLoad: bool = False, clearWhenDone: bool = False):
    length = _sameLineFloat("RDC=")
    chosen = _singleSelect.numericSerial(
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
        return length / (2 * _pi)


def RDC(length: float, clearOnLoad: bool = False, clearWhenDone: bool = False) -> float:
    chosen = _singleSelect.numericSerial(
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
        return length / (2 * _pi)


__all__ = ["newLineRDC", "sameLineRDC", "RDC"]
