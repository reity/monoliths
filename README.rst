=========
monoliths
=========

Python tool for automatically wrapping a multi-module Python library into a single portable module file.

|pypi| |travis|

.. |pypi| image:: https://badge.fury.io/py/monoliths.svg
   :target: https://badge.fury.io/py/monoliths
   :alt: PyPI version and link.

.. |travis| image:: https://travis-ci.com/reity/monoliths.svg?branch=master
    :target: https://travis-ci.com/reity/monoliths

Purpose
-------
This tool can assist with the implementation of an automated process that wraps a Python library consisting of multiple modules into a single portable module file.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install monoliths

The library can be imported in the usual way::

    import monoliths
    from monoliths import *

Conventions
-----------
Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    pylint monoliths

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the GitHub page for this library.

Versioning
----------
Beginning with version 0.1.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
