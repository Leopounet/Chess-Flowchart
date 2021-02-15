import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from enum import Enum

class Tags(Enum):

    """
    The list of all possible tags (see :doc:`StringReader.py <StringReader.py>` for more info).
    """

    NAMETAG_START = "$("
    NAMETAG_END = ")"

    CHECKMATE = "#"
    WHITE_ADV = "!W"
    BLACK_ADV = "!B"
    EQUIVALENT = "="
