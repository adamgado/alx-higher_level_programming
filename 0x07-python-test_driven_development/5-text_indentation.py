#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """add 2 lines after '.', '?' and ':'

    Args:
        text: string

    Raises:
        TypeError: text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for a in ".?:":
        text = (a + "\n\n").join(
            [line.strip(" ") for line in text.split(a)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
