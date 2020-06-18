"""Tool for assembling single-module libraries.

Python tool for automatically wrapping a multi-module Python
library into a single portable module file.
"""

from __future__ import annotations
import doctest

class monoliths():
    """
    Instance of a single-file library module.
    """

    def __init__(self: monoliths):
        pass

if __name__ == "__main__":
    doctest.testmod()
