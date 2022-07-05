#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print contents of a UTF8 text file to standard output."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
