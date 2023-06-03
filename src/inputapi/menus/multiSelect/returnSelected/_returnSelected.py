from ....otherFunc import clearScreen
from ....numerical import integer
from ....boolean import yesNo


def numeric(
    *args,
    confirmChoice: bool = True,
    showSelectedOnRefresh: bool = True,
    clearOnLoad: bool = False,
    cleanOnRefresh=False,
    clearWhenDone: bool = False,
    title: str = "Menu",
) -> list:

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
                    print(f"{serial}: *{arg}")
                    continue
                print(f"{serial}: {arg}")
            print("0: Done")

            print()
            selected = integer.newLineInt(
                "Multiple selection menu\nTo select an option input the letters next to it:",  # noqa: E501
                False,
                0,
                serial,
            )
            if selected != 0:
                if args[selected - 1] in options and options != [args[selected - 1]]:
                    index = options.index(args[selected - 1])
                    options.pop(index)
                elif showSelectedOnRefresh and args[selected - 1] not in options:
                    options.insert(selected - 1, args[selected - 1])
        if confirmChoice:
            confirmed = yesNo(
                ", ".join(options) + "\nConfirm choice?", clearOnLoad=cleanOnRefresh
            )
        else:
            confirmed = True

    if clearWhenDone:
        clearScreen.auto()

    return [x for x in args if x in options]


__all__ = ["numeric"]
