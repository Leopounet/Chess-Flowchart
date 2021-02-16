import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from enum import Enum

class GraphType(Enum):

    """
    All possible graph types.
    """
    DIGRAPH = ("digraph G {", "->")