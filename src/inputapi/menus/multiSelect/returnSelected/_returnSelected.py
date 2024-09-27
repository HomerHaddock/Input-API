from ....otherFunc import clearScreen
from ....numerical import integer
from ....boolean import yesNo


def selectionHandler(
    *args, selected: int, options: list, showSelectedOnRefresh: bool
) -> list:
    if not showSelectedOnRefresh:
        options.pop(selected - 1)
        return options

    if args[selected - 1] in options:
        index = options.index(args[selected - 1])
        options.pop(index)
    else:
        options.insert(selected - 1, args[selected - 1])

    return options


def numericSerial(
    *args,
    confirmChoice: bool = True,
    showSelectedOnRefresh: bool = True,
    allowNoSelection: bool = False,
    clearOnLoad: bool = False,
    cleanOnRefresh: bool = False,
    clearWhenDone: bool = False,
    title: str = "Menu",
) -> list:
    """numericSerial allows users to select multiple options

    A menu that asks users to select multiple options then returns the values
    (e.g. If a selected item was a list of floats then that is what is returned)
    All values are given an serial starting at 1 and increasing as more options show.

    Args:
        confirmChoice (bool, optional): Asks the user if the selection is correct. Defaults to True.
        showSelectedOnRefresh (bool, optional): Shows what the user has selected and hasn't. Defaults to True.
        clearOnLoad (bool, optional): Clears terminal before displaying. Defaults to False.
        cleanOnRefresh (bool, optional): Clears terminal on user selection. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal when finished. Defaults to False.
        title (str, optional): Title to be displayed. Defaults to "Menu".

    Returns:
        list: The *args that were selected by the user
    """  # noqa: E501

    if len(args) == 0:
        if allowNoSelection:
            return args
        raise SyntaxError(
            "No selectable options, give at least [1] option or set allowNoSelection to True"  # noqa: E501
        )

    if clearOnLoad:
        clearScreen.auto()

    confirmed = False
    while not confirmed:
        options = list(args)
        selected = -1
        while selected != 0:
            display = "\n"
            if cleanOnRefresh:
                display = ""
                clearScreen.auto()

            if title != "":
                display += "\u001b[30m\u001b[47m---%s---\u001b[0m" % title

            serial = 0
            for arg in args:
                if arg not in options and not showSelectedOnRefresh:
                    continue
                serial += 1
                if arg not in options:
                    display += "\n%s: *%s" % (serial, arg)
                    continue
                display += "\n%s: %s" % (serial, arg)
            display += "\n0: Done"

            display += "\n"  # Creates space between the options and the input
            selected = integer.newLineInt(
                display + "\nMultiple selection menu\nTo select an option input the number next to it:",  # noqa: E501
                allowNeg=False,
                min=0,
                max=serial,
            )
            if selected != 0:
                options = selectionHandler(
                    *args,
                    selected=selected,
                    options=options,
                    showSelectedOnRefresh=showSelectedOnRefresh,
                )

            if not showSelectedOnRefresh and len(options) == 0:
                selected = 0

        if len(options) == len(args) and not allowNoSelection:
            continue

        if confirmChoice:
            confirmed = yesNo(
                ("\n%s\nConfirm choice?" %
                 ([i for i in args if i not in options]))
                .replace("'", "")
                .replace("[", "")
                .replace("]", ""),
                clearOnLoad=cleanOnRefresh,
            )
        else:
            confirmed = True

    if clearWhenDone:
        clearScreen.auto()

    return [x for x in args if x not in options]  # type: ignore


__all__ = ["numericSerial"]
