from ..otherFunc.clearScreen import auto as _clearScreen
from ..strings import sameLineStr as _sameLineStr


def yesNo(
    request: str = "Yes or no?",
    *,
    allowNumeric: bool = True,
    default: int | str | None = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> bool:
    """yesNo asks a Yes or No question

    For Boolean input you ask a request and get a Boolean representing the users response while repeating if the user gives an invalid response

    Args:
        request (str, optional): The question to be written in the terminal for the user to answer. Defaults to empty string.
        default (int | str | None, optional): What will be returned if the user just presses enter. 0 or "y" means Y is default, 1 or "N" means N is default. Not case sensitive, and None means no default.
        allowNumeric (bool, optional): Allows the user to input a number along with the Y/n (Great for programs with a lot of numeric inputs). Defaults to True.
        clearOnLoad (bool, optional): Clears the terminal when running the function. Defaults to False.
        clearWhenDone (bool, optional): When the user gives the input it will clear the terminal. Defaults to False.

    Returns:
        response: True means the user said Yes, False for No
    """  # noqa: E501

    if clearOnLoad:
        _clearScreen()

    display = ["y", "n"]
    if default is not None:
        default = "yn".index(default.lower()) if isinstance(default, str) else default
        display[default] = display[default].capitalize()
    display = tuple(display)

    allowedInput = ["Y", "N", "y", "n"]
    numericMessage = ""
    if allowNumeric:
        numericMessage = "Numeric response allowed (%s=1, %s=2)\n" % display
        allowedInput.append("1")
        allowedInput.append("2")

    query = _sameLineStr(
        "%s%s[%s/%s]:" % (request + "\n" if request else "", numericMessage, *display),
        minLength=0 if default is not None else 1,
        maxLength=1,
        allowOnly="".join(allowedInput),
    )

    user = query.lower() in {"y", "1"}
    if len(query) == 0:
        user = True if not default else False

    if clearWhenDone:
        _clearScreen()

    return user


__all__ = ["yesNo"]
