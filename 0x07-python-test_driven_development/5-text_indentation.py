#!/usr/bin/python3
"""Module that Write a function that prints a text
  with 2 new lines after each of these characters:
  ., ? and :"""


def text_indentation(text):
    """a function that prints a text with
    2 new lines after each of these characters:
    ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    nl = True

    for c in text:
        if nl and c == ' ':
            continue

        nl = False

        print(c, end='')

        if c in ".?:":
            print("\n")
            nl = True
