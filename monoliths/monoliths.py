"""Tool for assembling single-module libraries.

Python tool for automatically wrapping a multi-module Python
library into a single portable module file.
"""

from __future__ import annotations
import doctest
import json

class monoliths():
    """
    Instance of a single-file library module.
    """

    @staticmethod
    def _requirements_concat(r1, r2):
        """Combine two sets of requirements."""
        return list(set(r1).union(set(r2)))

    def __init__(self: monoliths, paths=None, requirements=None):
        """Create empty base module."""
        self.paths = []
        self.requirements = []
        self.modules = []

        if paths is not None:
            self.extend(paths)

        if requirements is not None:
            self.requirements = requirements

    def append(self: monoliths, path: str, requirements=None) -> monoliths:
        """Add a module to current module being assembled."""
        requirements_ = [] if requirements is None else requirements

        with open(path, 'r') as module_file:
            self.paths.append(path)
            self.requirements = monoliths._requirements_concat(
                self.requirements, requirements_
            )
            self.modules.append(module_file.read())

    def extend(self: monoliths, paths: list, requirements=None) -> monoliths:
        """Add multiple modules to current module being assembled."""
        for path in paths:
            self.append(path, requirements)

    def concat(self: monoliths, other: monoliths) -> monoliths:
        """Concatenate two modules, returning a new module."""
        m = monoliths()
        m.paths = list(self.paths) + list(other.paths)
        m.requirements = monoliths._requirements_concat(
            self.requirements, other.requirements
        )
        m.modules = list(self.modules) + list(other.modules)
        return m

    def __add__(self: monoliths, other: monoliths) -> monoliths:
        """Concatenate two modules, returning a new module."""
        return self.concat(other)

    def emit(self: monoliths, path: str, transform_str=None):
        """Emit assembled module as a file with specified path."""
        with open(path, 'w') as module_file:

            # Make it possible to emit the merged module's requirements
            # via the command line.
            if len(self.requirements) > 0:
                requirements = [
                    "    " + line
                    for line in json.dumps(self.requirements, indent=4).split("\n")
                ]
                module_file.write('''if __name__ == "__main__":\n''')
                module_file.write('''    requirements = [\n''')
                module_file.write("\n".join(requirements[1:-1]) + '''\n    ]\n''')
                module_file.write('''    import sys\n''')
                module_file.write('''    if sys.argv[1:] == ["requirements"]:\n''')
                module_file.write('''        for r in requirements:\n''')
                module_file.write('''            print(r)\n''')
                module_file.write('''    if sys.argv[1:] == ["requirements.txt"]:\n''')
                module_file.write('''        with open("requirements.txt", "w") as f:\n''')
                module_file.write('''            f.write("\\n".join(requirements) + "\\n")\n''')
                module_file.write('''    exit(0)\n\n''')

            # Emit the contents of the constituent modules.
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
