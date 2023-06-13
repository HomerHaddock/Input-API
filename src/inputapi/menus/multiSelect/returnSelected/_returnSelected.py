from ....otherFunc import clearScreen
from ....numerical import integer
from ....boolean import yesNo


def numericSerial(
    *args,
    confirmChoice: bool = True,
    showSelectedOnRefresh: bool = True,
    clearOnLoad: bool = False,
    cleanOnRefresh: bool =False,
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
    
    if clearOnLoad:
        clearScreen.auto()

    confirmed = False
    while not confirmed:
        options = list(args)
        selected = -1
        while selected != 0:

            if cleanOnRefresh:
                clearScreen.auto()
            
            if title != "":
                print("\u001b[30m\u001b[47m---%s---\u001b[0m" % title)
            
            serial = 0
            for arg in args:
                if arg not in options and not showSelectedOnRefresh:
                    continue
                serial += 1
                if arg not in options:
                    print("%s: *%s" % (serial, arg))
                    continue
                print("%s: %s" % (serial, arg))
            print("0: Done")

            print()  # Creates space between the options and the input
            selected = integer.newLineInt(
                "Multiple selection menu\nTo select an option input the letters next to it:",  # noqa: E501
                allowNeg = False,
                min = 0,
                max = serial,
            )
            if selected != 0:
                if args[selected - 1] in options and options != [args[selected - 1]]:
                    index = options.index(args[selected - 1])
                    options.pop(index)
                elif showSelectedOnRefresh and args[selected - 1] not in options:
                    options.insert(selected - 1, args[selected - 1])
        
        if confirmChoice:
            confirmed = yesNo(
                "%s\nConfirm choice?", clearOnLoad=cleanOnRefresh
            )
        else:
            confirmed = True

    if clearWhenDone:
        clearScreen.auto()

    return [x for x in args if x in options]  # type: ignore


__all__ = ["numericSerial"]
