from ..otherFunc import clearScreen
import logging


def newLineStr(
    request: str = "Input a string:",
    *,
    minLength: int = 0,
    maxLength: int | None = None,
    allowOnly: str | None = None,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> str:
    if clearOnLoad:
        clearScreen.auto()

    if request != "":
        print(request)

    run = True
    while run:
        user = input(">")

        error = False
        if len(user) < minLength:
            error = True
            logging.warning(
                f"Input requires [{minLength}] characters or more, you entered [{len(user)}] characters"  # noqa: E501
            )
        if maxLength is not None:
            if len(user) > maxLength:
                error = True
                logging.warning(
                    f"Input requires [{maxLength}] characters or less, you entered [{len(user)}] characters"  # noqa: E501
                )
        if allowOnly is not None:
            for x in user:
                if x not in allowOnly:
                    error = True
                    if len(allowOnly) < 20:
                        logging.warning(
                            f"Input has invalid character [{x}], allowed characters are [{', '.join(x for x in allowOnly)}]"  # noqa: E501
                        )
                    elif len(allowOnly) > 25:
                        logging.warning(
                            f"Input has invalid character [{x}], allowed characters are [{', '.join(x for x in allowOnly[:20])} ... {', '.join(x for x in allowOnly[-5:])}]"  # noqa: E501
                        )
                    else:
                        logging.warning(
                            f"Input has invalid character [{x}], allowed characters are [{', '.join(x for x in allowOnly[:20])} ... {allowOnly[-1]}]"  # noqa: E501
                        )
                    break
        if error is False:
            run = False

    if clearWhenDone:
        clearScreen.auto()

    return user


def sameLineStr(
    request: str = "String=",
    *,
    minLength: int = 0,
    maxLength: int | None = None,
    allowOnly: str | None = None,
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
            logging.warning(
                f"Input requires [{minLength}] characters or more, you entered [{len(user)}] characters"  # noqa: E501
            )
        if maxLength is not None:
            if len(user) > maxLength:
                error = True
                logging.warning(
                    f"Input requires [{maxLength}] characters or less, you entered [{len(user)}] characters"  # noqa: E501
                )
        if allowOnly is not None:
            for x in user:
                if x not in allowOnly:
                    error = True
                    if len(allowOnly) < 20:
                        logging.warning(
                            f"Input has invalid character [{x}], allowed characters are [{', '.join(x for x in allowOnly)}]"  # noqa: E501
                        )
                    elif len(allowOnly) > 30:
                        logging.warning(
                            f"Input has invalid character [{x}], allowed characters are [{', '.join(x for x in allowOnly[:20])} ... {', '.join(x for x in allowOnly[-5:])}]"  # noqa: E501
                        )
                    else:
                        logging.warning(
                            f"Input has invalid character [{x}], allowed characters are [{', '.join(x for x in allowOnly[:20])} ... {allowOnly[-1]}]"  # noqa: E501
                        )
                    break
        if error is False:
            run = False

    if clearWhenDone:
        clearScreen.auto()

    return user


__all__ = ["newLineStr", "sameLineStr"]
