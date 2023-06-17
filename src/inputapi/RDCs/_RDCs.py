from math import pi as _pi

from ..menus import singleSelect as _singleSelect
from ..numerical.float import (
    newLineFloat as _newLineFloat,
)
from ..numerical.float import (
    sameLineFloat as _sameLineFloat,
)
from ..otherFunc.clearScreen import auto as _auto


def newLineRDC(
    *,
    clearOnLoad: bool = False,
    clearOnRefresh: bool = False,
    clearWhenDone: bool = False,
) -> float:
    """newLineRDC returns the radius of a circle given the radius, diameter, or circumference.

    This function will take user input with newLineFloat
    After the user selects the type of value they are inputting, the function will return the radius.

    Args:
        clearOnLoad (bool, optional): Clears terminal before loading. Defaults to False.
        clearOnRefresh (bool, optional): Clears terminal when switching inputs. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal when finished. Defaults to False.

    Returns:
        float: radius of a circle
    """  # noqa: E501

    if clearOnLoad:
        _auto()

    length = _newLineFloat("RDC:", clearOnLoad=clearOnLoad)

    print()

    chosen = _singleSelect.numericSerial(
        "Radius",
        "Diameter",
        "Circumference",
        clearOnLoad=clearOnRefresh,
        clearWhenDone=clearWhenDone,
        title="RDC",
    )

    if chosen == 1:
        return length
    elif chosen == 2:
        return length / 2
    elif chosen == 3:
        return length / (2 * _pi)


def sameLineRDC(
    *,
    clearOnLoad: bool = False,
    clearOnRefresh: bool = False,
    clearWhenDone: bool = False,
) -> float:
    """sameLineRDC returns the radius of a circle given the radius, diameter, or circumference.
    
    Asks for the radius, diameter, or circumference on the same line as the request.
    After the user selects the type of value they are inputting, the function will return the radius.
    Uses sameLineFloat
    
    Args:
        clearOnLoad (bool, optional): Clears terminal before loading. Defaults to False.
        clearOnRefresh (bool, optional): Clears terminal when switching inputs. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal when finished. Defaults to False.
    Returns:
        float: radius of a circle
    """  # noqa: E501
    length = _sameLineFloat("RDC=", clearOnLoad=clearOnLoad)

    print()
    
    chosen = _singleSelect.numericSerial(
        "Radius",
        "Diameter",
        "Circumference",
        clearOnLoad=clearOnRefresh,
        clearWhenDone=clearWhenDone,
        title="RDC",
    )

    if chosen == 1:
        return length
    elif chosen == 2:
        return length / 2
    elif chosen == 3:
        return length / (2 * _pi)


def RDC(
    length: float,
    *,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> float:
    """RDC takes a radius, diameter, or circumference and returns the radius.

    This function will take a radius, diameter, or circumference and return the radius
    After the user selects the type of value they are inputting, the function will return the radius

    Args:
        length (float): Length of radius, diameter, or circumference
        clearOnLoad (bool, optional): Clear terminal before asking. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal when finished. Defaults to False.

    Returns:
        float: radius of a circle
    
    Raises:
        TypeError: If length is not a float
    """  # noqa: E501
    
    if not isinstance(length, (float, int)):
        raise TypeError("length must be a float or int")
    
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
