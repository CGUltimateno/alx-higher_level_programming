#!/usr/bin/python3
"""Module for write_file method."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of
    characters written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)

        return len(text)
