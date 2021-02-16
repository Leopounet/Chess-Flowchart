import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from enum import Enum

class LinuxColors(Enum):
    """
    Coloring the output on Linux terminals.
    """
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    ORANGE = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    DEFAULT = "\033[39m"

class OtherColors(Enum):
    """
    Not coloring anything else.
    """
    BLACK = ""
    RED = ""
    GREEN = ""
    ORANGE = ""
    BLUE = ""
    MAGENTA = ""
    CYAN = ""
    DEFAULT = ""

class DotColor(Enum):
    """
    Some colors in dot files.
    """
    WHITE = "#ffffff"
    LIGHT_GRAY = "#cccccc"
    RED = "#ff0000"
    GREEN = "#00ff00"
    LIGHT_BLUE = "#aaaaff"
