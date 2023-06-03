# New imports for the 2.X structure
from . import boolean, menus, numerical, otherFunc, RDCs, strings  # noqa: F401

# 1.X.X support
from .otherFunc.clearScreen import auto as clearScreen  # noqa: F401
from .otherFunc.pause import standard as pause  # noqa: F401
from .RDCs import RDC  # noqa: F401
from .numerical.float import newLineFloat # noqa: F401
from .numerical.integer import newLineInt # noqa: F401
from .menus.singleSelect import numericSerial as menu # noqa: F401
from .boolean import yesNo # noqa: F401
from .strings import newLineStr  # noqa: F401

# Logging module import and config
import logging as _logging
_logging.basicConfig(format="%(levelname)s: %(message)s", level=_logging.WARNING)

__all__ = [x for x in dir() if "_" not in x]
