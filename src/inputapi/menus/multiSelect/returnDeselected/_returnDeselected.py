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
    """numericSerial allows users to select multiple options at once.

    A menu where users can select more than one option and what is left is returned.

    Args:
        confirmChoice (bool, optional): Allows user to reconsider choice when done. Defaults to True.
        showSelectedOnRefresh (bool, optional): Shows what the user selected as toggled options. Defaults to True.
        clearOnLoad (bool, optional): Clears terminal before displaying options. Defaults to False.
        cleanOnRefresh (bool, optional): Clears terminal when user selects option. Defaults to False.
        clearWhenDone (bool, optional): Clears terminal after user is done selecting. Defaults to False.
        title (str, optional): Title for the menu. Defaults to "Menu".

    Returns:
        list: All options not selected by user.
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
            print()
            confirmed = yesNo(
                ("%s\nConfirm choice?" %
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

    return [x for x in args if x in options]


__all__ = ["numericSerial"]
