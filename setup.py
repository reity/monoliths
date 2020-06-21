from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="monoliths",
    version="0.1.0",
    packages=["monoliths",],
    install_requires=[],
    license="MIT",
    url="https://github.com/reity/monoliths",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Python tool for automatically wrapping a multi-module " +\
                "Python library into a single portable module file.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    test_suite="nose.collector",
    tests_require=["nose"],
)
