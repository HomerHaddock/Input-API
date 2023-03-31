import os as _os


def auto():
    """auto clears terminal without need for input

    Based on the operating system this function will run the command used best for the terminal
    Windows will have "cls" used and all other operating systems will have "clear" run

    (This only supports Windows, MacOS, & Linux)

    No input required
    """
    _os.system("cls" if _os.name == "nt" else "clear")


def manual(OS: str):
    """manual clears terminal with the command based on the OS input

    Based on the operating system inputted it will run the terminal command for the specific
    Only supports Windows, MacOS, & Linux

    Args:
        OS (str): Operating system type for command (Not case-sensitive but relies on correct spelling)

    Raises:
        OSError: This will only raise when the operating system specified is not supported
    """
    OS = OS.lower()
    if OS == "windows":
        _os.system("cls")
    elif OS == "macos" or OS == "linux":
        _os.system("clear")
    else:
        raise OSError("Operating system incompatible")


__all__ = ["auto", "manual"]
