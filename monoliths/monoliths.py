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

    def __init__(self: monoliths, paths=None):
        """Create empty base module."""
        self.paths = []
        self.modules = []
        if paths is not None:
            self.extend(paths)

    def append(self: monoliths, path: str) -> monoliths:
        """Add a module to current module being assembled."""
        with open(path, 'r') as module_file:
            self.paths.append(path)
            self.modules.append(module_file.read())

    def extend(self: monoliths, paths: list) -> monoliths:
        """Add multiple modules to current module being assembled."""
        for path in paths:
            self.append(path)

    def concat(self: monoliths, other: monoliths) -> monoliths:
        """Concatenate two modules, returning a new module."""
        m = monoliths()
        m.paths = list(self.paths) + list(other.paths)
        m.modules = list(self.modules) + list(other.modules)
        return m

    def __add__(self: monoliths, other: monoliths) -> monoliths:
        """Concatenate two modules, returning a new module."""
        return self.concat(other)

    def emit(self: monoliths, path: str, transform_str=None):
        """Emit assembled module as a file with specified path."""
        with open(path, 'w') as module_file:
            for (i, m) in enumerate(self.modules):
                m = transform_str(m) if transform_str is not None else m
                module_file.write(m)
                if i < len(self.modules) - 1:
                    module_file.write("\n")

class exclude():
    """
    Delimiters to demarcate sections of modules to be excluded
    from the emitted consolidated module.
    """

    start = "exclude.start"
    end = "exclude.end"

if __name__ == "__main__":
    doctest.testmod()
